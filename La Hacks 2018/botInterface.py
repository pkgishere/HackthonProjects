import paho.mqtt.publish as publish


def command(str):
	return publish.single("anith/test",str,hostname="test.mosquitto.org")



def move(direction,value):
	payload = {
		"function":"move",
		"params":
			{
			"direction":direction,
			"value":value
			}
	}
	return command(str(payload))

def rotate(direction,value):
	payload = {
		"function":"rotate",
		"params":
			{
			"direction":direction,
			"value":value
			}
	}
	return command(str(payload))

def setLED(value):
	payload = {
		"function":"setLED",
		"params":
			{
			"value":value
			}
	}
	return command(str(payload))


def readCamera():
	payload = {
		"function":"readCamera",
		"params":{}
	}
	return command(str(payload))

def emotion():
	payload = {
		"function":"Emotion",
		"params":{}
	}
	return command(str(payload))

def detect():
	payload = {
		"function":"Detect",
		"params":{}
	}
	return command(str(payload))
