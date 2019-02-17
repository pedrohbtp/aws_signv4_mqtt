[![Build Status](https://travis-ci.com/pedrohbtp/aws_signv4_mqtt.svg?branch=master)](https://travis-ci.com/pedrohbtp/aws_signv4_mqtt)
[![Coverage Status](https://coveralls.io/repos/github/pedrohbtp/aws_signv4_mqtt/badge.svg?branch=master)](https://coveralls.io/github/pedrohbtp/aws_signv4_mqtt?branch=master)
# aws_signv4_mqtt
Functions to generate aws signature v4 to use with AWS IOT MQTT

I created this because I couldn't find a library to easily generate signed urls that you can use with amazon's MQTT for IOT in python.
All the libraries I could find would be to generate headers for HTTP requests and it wouldn't work with wss for MQTT.

Inspired by:
  * https://gist.github.com/prestomation/24b959e51250a8723b9a5a4f70dcae08
* https://gist.github.com/kn9ts/4b5a9942b6afbfc2534f2f14c87b9b54

# Installing

```bash
pip install aws-signv4-mqtt
```

# How to use use

There are two interfaces:
```python
aws_signv4_mqtt.generate_signv4_mqtt( iot_host, iot_region, access_key, secret_key)
```

Basic interface to created the signed url.

```python
aws_signv4_mqtt.generate_signv4_mqtt_boto( iot_host, iot_region)
```

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


# Testing your url

After you generate your url using AWS credentials with sufficient AWS IOT permissions, you can test it with any MQTT library.

For instance, you could execute the javascript code below:

```javascript
var mqtt = require('mqtt')
url = '<your_signed_url>'
port = 443
topic = '<your_topic>'
i = 0

var client  = mqtt.connect(url,
    {
        connectTimeout:5*1000,
        port: port,
    })
 
client.on('connect', function () {
  client.subscribe(topic, function (err) {
    if (!err) {
      client.publish(topic, 'Hello mqtt')
    }
  })
})
 
client.on('message', function (topic, message) {
  console.log(message.toString())
  i = i+1
  client.publish(topic, 'Hello mqtt '+String(i))
})
```


