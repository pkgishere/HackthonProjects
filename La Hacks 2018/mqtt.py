import paho.mqtt.client as mqtt
def on_connect(client, userdata, flags, rc):
    print(str(rc))
    client.subscribe("anith/test")
    client.subscribe("anith/topic")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    if msg.payload == "Hello":
        print("Received msg #1")

    if msg.payload == "World!":
        print("Received msg #2")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()
