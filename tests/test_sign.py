import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from subprocess import call
import aws_signv4_mqtt
def test_generate_signv4_mqtt_boto():
    url = aws_signv4_mqtt.generate_signv4_mqtt_boto( os.environ['iot_host'], os.environ['iot_region'])
    result = call(["node", "mqtt-test.js", url]) 
    assert result == 0