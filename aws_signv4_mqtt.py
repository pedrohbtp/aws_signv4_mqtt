import urllib
import sys, os, base64, datetime, hashlib, hmac 
from boto3 import session
def sign(key, msg):
    return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

def getSignatureKey(key, dateStamp, regionName, serviceName):
    kDate = sign(('AWS4' + key).encode('utf-8'), dateStamp)
    kRegion = sign(kDate, regionName)
    kService = sign(kRegion, serviceName)
    kSigning = sign(kService, 'aws4_request')
    return kSigning

def generate_signv4_mqtt_boto( iot_host, iot_region):
    ''' Gets the credentials from the environment using boto3 and use them 
    to create the signed url
    '''
    boto_session = session.Session()
    credentials = boto_session.get_credentials()
    return generate_signv4_mqtt( iot_host, iot_region, credentials.access_key, credentials.secret_key)

def generate_signv4_mqtt( iot_host, iot_region, access_key, secret_key):
    '''  
    Generates the signed url to be used with amazon MQTT
    reference1: https://gist.github.com/prestomation/24b959e51250a8723b9a5a4f70dcae08
    reference2: https://gist.github.com/kn9ts/4b5a9942b6afbfc2534f2f14c87b9b54
    '''
    method = 'GET'
    service = 'iotdevicegateway'
    host = iot_host
    region = iot_region
    canonical_uri = '/mqtt' 
    # Create a date for headers and the credential string
    algorithm = 'AWS4-HMAC-SHA256'
    t = datetime.datetime.utcnow()
    amzdate = t.strftime('%Y%m%dT%H%M%SZ')
    datestamp = t.strftime('%Y%m%d') # Date w/o time, used in credential scope
    credential_scope = datestamp + '/' + region + '/' + service + '/' + 'aws4_request'
    canonical_querystring = {
        'X-Amz-Algorithm': algorithm,
        'X-Amz-Credential': access_key+ '/' +credential_scope,
        'X-Amz-Date': amzdate,
        'X-Amz-SignedHeaders': 'host'

    }
    canonical_headers = 'host:' + host + '\n'
    payload_hash = hashlib.sha256(''.encode('utf-8')).hexdigest()
    canonical_request = method + '\n' + canonical_uri + '\n' + urllib.parse.urlencode(canonical_querystring) + '\n' + canonical_headers + '\nhost\n' + payload_hash
    string_to_sign = algorithm + '\n' +  amzdate + '\n' +  credential_scope + '\n' +  hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()
    signing_key = getSignatureKey(secret_key, datestamp, region, service)
    # Sign the string_to_sign using the signing_key
    signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()
    return 'wss://'+host+canonical_uri+'?'+urllib.parse.urlencode(canonical_querystring)+'&X-Amz-Signature=' + signature