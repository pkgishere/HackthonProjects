import requests
actionUrl = 'http://35.188.38.8/lahacks'
import os
import dialogFlow
import pyrebase


config = {
	"apiKey": "AIzaSyBfSdJP-rwtyADckvIVe1GpO7sfGnkcpdo",
	"authDomain": "newagent-1-f8001.firebaseapp.com",
	"databaseURL": "https://newagent-1-f8001.firebaseio.com",
	"storageBucket": "newagent-1-f8001.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()



def writeToFile(filename,method,text):
	with open(filename, method) as file:
		file.write(text)

def clearFile(filename):
	try:
		os.remove(filename)
	except:
		f = open(filename, "w+")
		f.close()

def findCustomCommand(intent):
	allCommands = db.child("commands").get()
	for command in allCommands.each():
		if command.val()['Name'] == intent:
			return(command.val())
	return None
	# {name": "Mortimer 'Morty' Smith"}

def executeCommand(command):
	for action in command['actions']:
		dialogFlow.postQuery(action)
		# print(action)

# print(findCustomCommand('make_pizza'))

class CustomCommand():
	def __init__(self,commandName):
		self.commandName = commandName
		self.linkedIntent = self.createIntent()
		self.reqs = []
		self.actions = []

	def createIntent(self):
		dialogFlow.postIntent(self.commandName)


	def saveCommand(self):
		self.command = {
			"Name": self.commandName.replace(' ','_'),
			"actions": self.actions,
			"linkedIntent": self.linkedIntent
		}

		db.child("commands").push(self.command)

