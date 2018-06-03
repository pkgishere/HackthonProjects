from __future__ import print_function
import json
import dateutil.parser
from flask import Flask,request,make_response,session
import logging
from logging import Formatter, FileHandler
from time import gmtime, strftime
import urllib
import ast
import getocr as textRead
import time
import requests
app=Flask(__name__)

isListening = False

@app.route('/bitcamp',methods=['POST'])
def BITCAMP():
        print("REQUEST:"+str(request))
        req = request.get_json(silent=True, force=True)
        req = req["body"]
        print(json.dumps(req,indent=4))
        r1=processRequest(req)
        r=CreateReply(r1)
    	r = make_response(r)
        r.headers['Content-Type'] = 'application/json'        
        return r

def CreateReply(reply):
    respo = {"response": reply}
    return json.dumps(respo)

def bufferStore(reply):
    with open('data.json', 'w') as outfile:
        json.dump(reply, outfile)

def readBufferStore():
    with open('data.json') as dataFile:
        data = json.load(dataFile)
    return data

def processRequest(req):
	intent = req['queryResult']['intent']['displayName']
	print(intent)
        if(intent == "HiReply"):
            return "Welcome to MaryLand"
        if(intent == "TakeAPhoto" ):
            reply = ast.literal_eval(textRead.performOCR())
            bufferStore(reply)
            ldaKeys = reply["ldakeyws"]
            answer = []
            for i in ldaKeys:
                answer.append(i[0])
            responseTemplate = "This document is about {0} and {1}. Do you want me to read the complete document ?".format(answer[0], answer[1])
            return responseTemplate
        if(intent == "ReadFeedBack"):
            FeedBack= req["queryResult"]["parameters"]["FeedBack"]
            if(FeedBack=="summarize" or FeedBack=="Yes"):
                jsonData = readBufferStore()

            if(FeedBack=="summarize"):
                responseTemplate = str(jsonData["summary"])
            elif(FeedBack == "Yes"):
                responseTemplate = str(jsonData["text"])
            else:
                responseTemplate = "Ok ! Can I help you in any other way ?"
            print(responseTemplate)
            return responseTemplate
        if(intent == "TimeRangeSearch"):
            datePeriod = req["queryResult"]["parameters"]["date-period"]
            startDate = dateutil.parser.parse(datePeriod['startDate']).strftime('%s')
            endDate = dateutil.parser.parse(datePeriod['endDate']).strftime('%s')
            print (startDate, endDate)
            startDate = str(startDate)
            endDate = str(endDate)
            requestUrl = "https://webhooks.mongodb-stitch.com/api/client/v2.0/app/devilseye-vlwxv/service/getArticle/incoming_webhook/webhook0?secret=ishan&startDate={0}&endDate={1}".format(startDate, endDate)
            print (requestUrl)
            data = requests.get(requestUrl)
            print(data.text)
        else:
            return "Can you please say that again, there is so much noise in background ?"

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

