from datetime import datetime
from termcolor import cprint, colored
import math
import colorama
import requests
import json
colorama.init()

## normal logging function - time and text
def log(text):
	print("[{}] - {}".format(stamp(), text))

## colored logging function - time and text in color
def cLog(value, color):
	text = colored(value, color)
	print('[{}] - {}'.format(stamp(), text))

def taskLog(tasknum,text):
	print("[Task {}] - [{}] - {}".format(str(tasknum),stamp(), text))

## colored logging function - time and text in color
def taskCLog(tasknum,value, color):
	text = colored(value, color)
	print('[Task {}] - [{}] - {}'.format(str(tasknum),stamp(), text))
## colored printing function - text in color
def cPrint(value, color):
	text = colored(value, color)
	print(text)

## used to get the time wrapped in square brackets
def stamp():
    timestamp = str(datetime.now().strftime("%H:%M:%S.%f")[:-3])
    return timestamp

## just fetches the time (no square brackets)
def rawStamp():
	timestamp = datetime.now().strftime("%H:%M:%S")
	return timestamp



def generateColor(profit):
	r = math.floor((255 * (150 - profit)) / 75)
	g = math.floor((255 * profit) / 75)
	b = 0
	r = clamp(r,0,255)
	g = clamp(g,0,255)
	b = clamp(b,0,255)
	print(r,g,b)
	hexColor = '%02x%02x%02x' % (r,g,b)
	return hexColor
def clamp(n, minn, maxn):
	return max(min(maxn, n), minn)

def postHook(jsonData,url):
	response = requests.post(url, data=json.dumps(jsonData),headers={'Content-Type': 'application/json'})
	if response.status_code != 200:
		print('An Error Occured: [{}]'.format(response.status_code))
	else:
		print('Sent Hook')
