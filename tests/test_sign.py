import sys
from subprocess import call
sys.path.append('..')
import aws_signv4_mqtt
import os

def test_generate_signv4_mqtt_boto():
    url = aws_signv4_mqtt.generate_signv4_mqtt_boto( os.environ['iot_host'], os.environ['iot_region'])
    result = call(["node", "mqtt-test.js", url]) 
    assert result == 0