import requests
import random
import getSameSentences
import requests
import json

apiUrl = 'https://api.dialogflow.com/v1/query?v=20150910'

headers = {
	"Authorization":"Bearer f788235201f44da3b4a569cbd5b39286",
	"Content-Type":"application/json"
}
intentHeaders = {"Authorization": "Bearer f72718e7f48344ecada7762effb5e834",
		"Content-Type" : "application/json"
		}
def postQuery(text):
	payload = {
		"lang": "en",
		"query":text,
		"sessionId": "12345"
	}
	r = requests.post(apiUrl,data=json.dumps(payload),headers=headers)
	# print(r.text)
	print('posted query - ' + text)


def postIntent(Sentence):
	list = getSameSentences.createSimilarSentences(Sentence)
	training=[]
	# print(list)

	for i in list:
		j={	"data":[
						{
							"text":i
						}
					],
			'isTemplate' : 'false'
		}
		training.append(j)

	intent ={
		"name" : list[0].replace(" ","_"),
		'auto' : 'true',
		'contexts' : [],
		'templates' : [],
		'userSays' :training,
		'responses' : [
				{
					'resetContexts' : 'false',
					'action' : '',
					'affectedContexts' : [],
					'parameters' : [],
					'speech' : "Ok, performing " + str(list[0])
				}
			],
			'priority' : 500000,
	"webhookForSlotFilling": 'false',
	"webhookUsed": 'true'
	}

	intentUrl="https://api.dialogflow.com/v1/intents?v=20150910"
	r = requests.post(intentUrl,data=json.dumps(intent),headers=intentHeaders)
	# print(r.status_code)
	# print(r.text)
	print('posted intent - ' + 	(list[0].replace(" ","_"))
)

# postIntent('take a piss')
