import sys
import logging
import random
import json
from base64 import b64encode

import paho.mqtt.client as mqtt

# Get these credentials from LoRaWAN, instructions are in the README.md
USER = "xxxxxxxxxxxxxx@ttn"
PASSWORD = "NNSXS.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
PUBLIC_TLS_ADDRESS = "nam1.cloud.thethings.network"
PUBLIC_TLS_ADDRESS_PORT = 8883
DEVICE_ID = "eui-XXXXXXXXXXXXXXXXXXXXXX"

# Quality of Service (QoS)
QOS = 0

# Generate client ID with pub prefix randomly
CLIENT_ID = f"python-mqtt-{random.randint(0, 1000)}"

msg_string = "hello world"


def stop(client):
    client.disconnect()
    print("\nExit")
    sys.exit(0)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("\nConnected successfully to MQTT broker")
    else:
        print("Failed to connect, return code %d\n", rc)


def on_subscribe(client, userdata, mid, granted_qos):
    print(f"\nSubscribed with message id (mid) = {str(mid)} and QoS = {str(granted_qos)}")


def on_disconnect(client, userdata, rc):
    print(f"\nDisconnected with result code = {str(rc)}")


def on_log(client, userdata, level, buf):
    print(f"\nLog: {buf}")
    logging_level = client.LOGGING_LEVEL[level]
    logging.log(logging_level, buf)


print("Create new mqtt client instance")
mqttc = mqtt.Client(CLIENT_ID)

print("Assign callback functions")
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_disconnect = on_disconnect
mqttc.on_log = on_log

# Setup authentication from settings above
mqttc.username_pw_set(USER, PASSWORD)

# Enable encryption of messages
mqttc.tls_set()

print(f"Connecting to broker: {PUBLIC_TLS_ADDRESS}:{str(PUBLIC_TLS_ADDRESS_PORT)}")
mqttc.connect(PUBLIC_TLS_ADDRESS, PUBLIC_TLS_ADDRESS_PORT, 60)


try:
    topic = f"v3/{USER}/devices/{DEVICE_ID}/down/push"
    print(f"Subscribe to topic {topic} with QoS = {str(QOS)}")
    mqttc.subscribe(topic, QOS)
    print(f"Publishing message to topic {topic} with QoS = {str(QOS)}")
    # Most embedded systems use hexadecimal values, convert msg string to this format
    hexadecimal_payload = msg_string.encode().hex()
    print(f"Hex value of msg string is {hexadecimal_payload}, {sys.getsizeof(hexadecimal_payload)} bytes long")
    fport = 3

    # Now Convert hexadecimal payload to base64
    b64 = b64encode(bytes.fromhex(hexadecimal_payload)).decode()
    print(f"Convert hexadecimal_payload: {hexadecimal_payload} to base64: {b64}")

    payload = {"downlinks": [{"f_port": str(fport), "frm_payload": b64, "priority": "NORMAL"}]}
    msg = json.dumps(payload)

    result = mqttc.publish(topic, msg, QOS)

    # result: [0, 2]
    status = result[0]
    if status == 0:
        print(f"Send {payload} to topic {topic}")
    else:
        print("Failed to send message to topic {topic}")

except Exception as e:
    print(f"Can not subscribe or publish to topic with error {e}")
    stop(mqttc)

