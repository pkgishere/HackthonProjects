import paho.mqtt.publish as publish


publish.single("anith/test", "Led", hostname = "test.mosquitto.org")
publish.single("anith/topic", "Forward", hostname = "test.mosquitto.org")
publish.single("avyay/test", "Left", hostname = "test.mosquitto.org")
publish.single("avyay/topic", "Right", hostname = "test.mosquitto.org")

print("Done")  