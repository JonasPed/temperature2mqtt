import Adafruit_DHT
import json
import paho.mqtt.client as mqtt
import time
import argparse

def on_connect(client, userdata, flags, rc):
    pass

parser = argparse.ArgumentParser(description="DHT22 temperatre to MQTT")
parser.add_argument("-host", required=True)
parser.add_argument("-username")
parser.add_argument("-password")
parser.add_argument("-pin", required=True)
parser.add_argument("-topic", required=True)

args = parser.parse_args()
print(type(args))
print(args.host)
print(args.username)

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.connect(args.host)
mqtt_client.loop_start()

sensor = Adafruit_DHT.DHT22

DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, args.pin)
    data = dict()
    data['temperature'] = temperature
    data['humidity'] = humidity

    mqtt_client.publish(args.topic , json.dumps(data))
    print(temperature)

    time.sleep(30)
