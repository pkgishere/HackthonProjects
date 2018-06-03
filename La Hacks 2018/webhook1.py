from __future__ import print_function
import json
from flask import Flask,request,make_response,session
import logging
from logging import Formatter, FileHandler
from time import gmtime, strftime
import botInterface as bot
import customCommand as cc
app=Flask(__name__)

isListening = False

@app.route('/lahacks',methods=['POST'])
def LaHacks():
	# app.logger.debug("Inside LAHACKS FUNCTION")
	req=request.get_json(silent=True, force=True)
	# app.logger.debug("Request Json:"+ str(req))
	# pprint(req)
	res = processRequest(req)

	# app.logger.debug("Response json:\n"+str(res))

	r = make_response(res)
	r.headers['Content-Type'] = 'application/json'
	return r

def parseMove(context):
	direction = context['parameters']['direction']
	number = int(context['parameters']['number'])
	bot.move(direction, number)
	return buildResponse('Ok, moving {} units {}!'.format(number, direction))

def parseRotation(context):
	direction = context['parameters']['rotationValues']
	number = int(context['parameters']['temperature']['amount'])

	bot.rotate(direction, number)
	return buildResponse('Ok, rotating {} degrees {}!'.format(number, direction))

def parseLED(context):
	state = context['parameters']['LedState']
	bot.setLED(state)
	return buildResponse('Ok, turning LED {}!'.format(state))

def processRequest(req):
	global isListening
	global customCommand
	# pprint(req)
	intent = req['queryResult']['intent']['displayName']
	queryText = req['queryResult']['queryText']
	print(intent)
	if intent == 'Learning_Stop':
		isListening = False
		customCommand.saveCommand()
		return buildResponse('Ok, got it!')
	elif isListening:
		customCommand.actions.append(queryText)
		print(customCommand.actions)
		return buildResponse('Ok, learning: {}!'.format(queryText))
	elif intent == 'HiReply':
		return buildResponse('this is a hiReply')
	elif intent == 'Move':
		context = detectcontext(req,'movement')
		return parseMove(context)
	elif intent == 'LedTrigger':
		context = detectcontext(req,'ledtrigger')
		return parseLED(context)
	elif intent == 'Rotation':
		context = detectcontext(req,'rotate')
		return parseRotation(context)
	elif intent == 'Detect':
		bot.detect()
		return buildResponse('Ok, detecting my environment')

	elif intent == 'Emotion':
		bot.emotion()
		return buildResponse('Ok, detecting emotion')
	elif intent == 'ReadCamera':
		bot.readCamera()
		return buildResponse('Ok, reading from camera')
	elif intent == 'Learning_Begins':
		isListening = True
		context = detectcontext(req,'learning')
		commandName = context['parameters']['any']
		customCommand = cc.CustomCommand(commandName)
		return buildResponse('Ok, what should i learn?')
	else:
		searchedCommand = cc.findCustomCommand(intent)
		if searchedCommand != None:
			cc.executeCommand(searchedCommand)
			return buildResponse('ok! {}'.format(intent))
		else:
			return buildResponse("Not sure what you're saying?")




def detectcontext(req,targetContext):
	for context in req['queryResult']['outputContexts']:
		contextName = context['name'].split('/')[-1]
		if contextName == targetContext:
			return context
	return None

def pprint(text):
	print(json.dumps(text,indent=4))

def buildResponse(reply):
	response = {
		"fulfillmentText":reply
	}
	return json.dumps(response)


if __name__ == '__main__':
	file_handler = FileHandler('output.log')
	handler = logging.StreamHandler()
	file_handler.setLevel(logging.DEBUG)
	handler.setLevel(logging.DEBUG)
	file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
	handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
	app.logger.addHandler(handler)
	app.logger.addHandler(file_handler)
	app.logger.warning('Server started at '+strftime("%Y-%m-%d %H:%M:%S", gmtime()) )
	app.run(host='0.0.0.0',port=80,debug=False)
	app.logger.debug('Server stoped at '+strftime("%Y-%m-%d %H:%M:%S", gmtime()) )




