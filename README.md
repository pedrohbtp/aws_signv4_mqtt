# aws_signv4_mqtt
Functions to generate aws signature v4 to use with AWS IOT MQTT

I created this because I couldn't find a library to easily generate signed urls that you can use with amazon's MQTT for IOT in python.
All the libraries I could find would be to generate headers for HTTP requests and it wouldn't work with wss for MQTT.

Inspired by:
  * https://gist.github.com/prestomation/24b959e51250a8723b9a5a4f70dcae08
* https://gist.github.com/kn9ts/4b5a9942b6afbfc2534f2f14c87b9b54


# How to use use

There are two interfaces:

**generate_signv4_mqtt( iot_host, iot_region, access_key, secret_key)**

Basic interface to created the signed url.

**generate_signv4_mqtt_boto( iot_host, iot_region)**

Gets the credentials from your environment or iam role internally using boto3.

# Examples

```python
import aws_signv4_mqtt
print(aws_signv4_mqtt.generate_signv4_mqtt('<your_iot>.iot.us-east-1.amazonaws.com', 'us-east-1', '<aws_access_key>', '<aws_secret>'))
```
Prints something like:
```
wss://<your_iot>.iot.us-east-1.amazonaws.com/mqtt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=%3Caws_access_key%3E%2F20190216%2Fus-east-1%2Fiotdevicegateway%2Faws4_request&X-Amz-Date=20190216T115653Z&X-Amz-SignedHeaders=host&X-Amz-Signature=92bfc2b5a77489c5786a820044bf6c8ccb3c2f9b40c1d6a5f016b4d9c8662a5e
```


