"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function
import boto3
import math
import time
from math import sqrt
from time import sleep
from decimal import *
explain={}



# --------------- Helpers that build all of the responses ----------------------

    
    
def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def solveLogicStart(intent, session):
    count=0
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    client = boto3.client('dynamodb', region_name='us-east-1')
    session_attributes = {}
    card_title = 'Solve Logic Begins'
    speech_output = 'Welcome to Explain logic. Say your first statement'
    
    createTable1()
    createTable2()
    createTable3()
    createTable4()
    
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
   
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))
    
def createTable1():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    client = boto3.client('dynamodb', region_name='us-east-1')
    tableDoesNotExist=0
    try:
        response = client.describe_table(TableName='FindLogic')  
    except:
        tableDoesNotExist=1
    if tableDoesNotExist==1:
        table1 = dynamodb.create_table(TableName='FindLogic',
                                      KeySchema=[{'AttributeName': 'name',
                                      'KeyType': 'HASH'}],
                                      AttributeDefinitions=[{'AttributeName': 'name'
                                      , 'AttributeType': 'S'}],
                                      ProvisionedThroughput={'ReadCapacityUnits': 10,
                                      'WriteCapacityUnits': 10})
    else:                                      
        response=client.delete_table(TableName='FindLogic')
        while(1):
            try:
                response = client.describe_table(TableName='FindLogic')  
            except:
                break
        table1 = dynamodb.create_table(TableName='FindLogic',
                                      KeySchema=[{'AttributeName': 'name',
                                      'KeyType': 'HASH'}],
                                      AttributeDefinitions=[{'AttributeName': 'name'
                                      , 'AttributeType': 'S'}],
                                      ProvisionedThroughput={'ReadCapacityUnits': 10,
                                      'WriteCapacityUnits': 10})
    
    table1 = dynamodb.Table('FindLogic')
    

def createTable2():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    client = boto3.client('dynamodb', region_name='us-east-1')
    
    tableDoesNotExist=0
    try:
        response = client.describe_table(TableName='Direction')  
    except:
        tableDoesNotExist=1
    if tableDoesNotExist==1:
        table2 = dynamodb.create_table(TableName='Direction',
                                      KeySchema=[{'AttributeName': 'snum',
                                      'KeyType': 'HASH'}],
                                      AttributeDefinitions=[{'AttributeName': 'snum'
                                      , 'AttributeType': 'N'}],
                                      ProvisionedThroughput={'ReadCapacityUnits': 10,
                                      'WriteCapacityUnits': 10})
    else:                                      
        response=client.delete_table(TableName='Direction')
        while(1):
            try:
                response = client.describe_table(TableName='Direction')  
            except:
                break
        table2 = dynamodb.create_table(TableName='Direction',
                                      KeySchema=[{'AttributeName': 'snum',
                                      'KeyType': 'HASH'}],
                                      AttributeDefinitions=[{'AttributeName': 'snum'
                                      , 'AttributeType': 'N'}],
                                      ProvisionedThroughput={'ReadCapacityUnits': 10,
                                      'WriteCapacityUnits': 10})
    table2 = dynamodb.Table('Direction')
    

def createTable3():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    client = boto3.client('dynamodb', region_name='us-east-1')
    
    tableDoesNotExist=0
    try:
        response = client.describe_table(TableName='Statement')  
    except:
        tableDoesNotExist=1
    if tableDoesNotExist==1:
        table3 = dynamodb.create_table(TableName='Statement',
                                      KeySchema=[{'AttributeName': 'sno',
                                      'KeyType': 'HASH'},{'AttributeName': 'skey','KeyType': 'RANGE'}],
                                      AttributeDefinitions=[{'AttributeName': 'sno'
                                      , 'AttributeType': 'N'}, {'AttributeName': 'skey','AttributeType': 'N'}],
                                      ProvisionedThroughput={'ReadCapacityUnits': 10,
                                      'WriteCapacityUnits': 10})

    else:                                      
        response=client.delete_table(TableName='Statement')
        while(1):
            try:
                response = client.describe_table(TableName='Statement')  
            except:
                break
        table3 = dynamodb.create_table(TableName='Statement',
                                      KeySchema=[{'AttributeName': 'sno',
                                      'KeyType': 'HASH'},{'AttributeName': 'skey','KeyType': 'RANGE'}],
                                      AttributeDefinitions=[{'AttributeName': 'sno'
                                      , 'AttributeType': 'N'}, {'AttributeName': 'skey','AttributeType': 'N'}],
                                      ProvisionedThroughput={'ReadCapacityUnits': 10,
                                      'WriteCapacityUnits': 10})
    table3 = dynamodb.Table('Statement')
	
def createTable4():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    client = boto3.client('dynamodb', region_name='us-east-1')
    
    tableDoesNotExist=0
    try:
        response = client.describe_table(TableName='Age_Logic')  
    except:
        tableDoesNotExist=1
    if tableDoesNotExist==1:
        table4 = dynamodb.create_table(TableName='Age_Logic',
                                      KeySchema=[{'AttributeName': 'Name',
                                      'KeyType': 'HASH'}],
                                      AttributeDefinitions=[{'AttributeName': 'Name'
                                      , 'AttributeType': 'S'}],
                                      ProvisionedThroughput={'ReadCapacityUnits': 10,
                                      'WriteCapacityUnits': 10})
    else:                                      
        response=client.delete_table(TableName='Age_Logic')
        while(1):
            try:
                response = client.describe_table(TableName='Age_Logic')  
            except:
                break
        table4 = dynamodb.create_table(TableName='Age_Logic',
                                      KeySchema=[{'AttributeName': 'Name',
                                      'KeyType': 'HASH'}],
                                      AttributeDefinitions=[{'AttributeName': 'Name'
                                      , 'AttributeType': 'S'}],
                                      ProvisionedThroughput={'ReadCapacityUnits': 10,
                                      'WriteCapacityUnits': 10})
    table4 = dynamodb.Table('Age_Logic')

    

def solveLogicStatementEnd(intent, session):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    
    table1 = dynamodb.Table('FindLogic')
    table2 = dynamodb.Table('Direction')
    table3 = dynamodb.Table('Statement')
    table4 = dynamodb.Table('Age_Logic')
    try:
        table1.delete()
        table2.delete()
        table4.delete()
        table3.delete()
    except:
        print("table do not exist")
    card_title = 'Solve Logical Problem End'
    speech_output = 'Thank You!'
    session_attributes = {}
    should_end_session = True
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
                          

def solveLogicArithmetic(intent, session):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table1 = dynamodb.Table('FindLogic')
    card_title = 'Explain Logic Books'
    person = intent['slots']['Name']
    quantity = intent['slots']['Quantity']['value']
    person_db = initPerson1(person, quantity)
    a=intent['slots']['Things']['value']
    c=str(quantity)
    explain=  person_db['name'] + ' has ' + c + ' number of ' +  a + '.';
    
    putTable1(person_db)
    putTable3(explain)
    
    speech_output = 'Ok. Next statement please.'
    session_attributes = {}
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
                          

def initPerson1(person, quantity):
    quantity = float(quantity)
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table1 = dynamodb.Table('FindLogic')
    namee = person['value']
    response = table1.get_item(Key={'name': namee})
    if 'Item' in response:
        person_db = response['Item']
        person_db['value'] = quantity
        return person_db
    else:
        person['name'] = namee
        person['value'] = format(quantity, '.15g')
        return person
        
def putTable1(person):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table1 = dynamodb.Table('FindLogic')
    result=table1.scan()
    count=result['Count']+1
    person['name'] = person['name'].encode('ascii', 'ignore')
    response = table1.get_item(Key={'name': person['name']})
    if 'Item' in response:
        table1.delete_item(
            Key={
                'name': person['name']
            })
            
    table1.put_item(Item={'sno':count,'value': format(float(person['value']), '.15g'), 'name': person['name']})
    
def putTable3(explain):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table3 = dynamodb.Table('Statement')
    result=table3.scan()
    c=result['Count']
    c=c+1;
    response = table3.get_item(Key={'sno': c,'skey':c})
    if 'Item' in response:
        table3.delete_item(
            Key={
                'sno': c,
                'skey':c
            })
    table3.put_item(Item={'sno': c, 'sentence': explain,'skey':c})
    
def solveLogicArithmeticExchange(intent, session):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table1 = dynamodb.Table('FindLogic')
    card_title = 'Explain Logic Exchange'
    session_attributes = {}
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    person1 = intent['slots']['Main_User']
    person2 = intent['slots']['Secondary_User']
    quantity = intent['slots']['Quantity']['value']
    a = intent['slots']['Things']['value']
    person_db1 = initPerson2(person1, quantity, 1)
    print(person_db1)
    
    person_db2 = initPerson2(person2, quantity, 0)
    print(person_db2)
    
    if person_db1 == -1 or person_db2 == -1:
        return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          "Wrong Inputs", reprompt_text,
                          should_end_session))
    pname1 = intent['slots']['Main_User']['value']
    pname2 = intent['slots']['Secondary_User']['value']
    explain = 'Since, ' + pname1  + ' has given ' + str(quantity)  + ' ' + a +' to ' + pname2  + '. Therefore now, ' +  pname1 + ' has ' + str(person_db2['value'])  +' ' + str(a) + ' and ' + pname2 + ' has '+ str(int(person_db1['value'])) +' ' + str(a)
    putTable1(person_db1)
    putTable1(person_db2)
    putTable3(explain)
    speech_output = 'Ok. Next statement please.'
    
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
                          

def initPerson2(person_db, quantity, op):
    quantity = float(quantity)
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table1 = dynamodb.Table('FindLogic')
    namee = person_db['value']
    print (namee)
    response = table1.get_item(Key={'name': namee})
    if 'Item' in response:
        person_db = response['Item']
        if op==1:
            person_db['value'] = float(person_db['value'])+quantity
        elif op==0:
            person_db['value'] = float(person_db['value'])-quantity
        return person_db
    else:

        return -1
        
def solveLogicArithmeticRelativeMore(intent,session):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table1 = dynamodb.Table('FindLogic')
    card_title = 'Solve Logic Books'
    session_attributes = {}
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    person1 = intent['slots']['Main_User']
    person2 = intent['slots']['Secondary_User']
    quantity = intent['slots']['Quantity']['value']

    person_db1 = initPerson3(person1)
    person_db2 = initPerson4(person2)
    speech_output = "Ok. Noted. Next Statement?"
    if person_db1 == -1 or person_db2 == -1:
        return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          "Wrong Inputs", reprompt_text,
                          should_end_session))

    person_db1['value'] = float(person_db2['value'])+float(quantity)
    #explain="Since, " + person_db1['name'] +' has ' + str(quantity) + ' more than ' + person_db2['name'] + '. So If ' + person_db2['name'] + ' has ' + str(person_db2['value']) +' ' + intent['slots']['Things']['value'] + ' then as per the statement ' + person_db1['name'] + ' will have ' + str(int(person_db1['value'])) + ' ' + intent['slots']['Things']['value'];  
    putTable1(person_db1)
    #putTable3(explain)
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
                          
                          

def initPerson3(person):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table1 = dynamodb.Table('FindLogic')
    namee = person['value']
    response = table1.get_item(Key={'name': namee})
    if 'Item' in response:
        person_db = response['Item']
        return person_db
    else:

        person['name'] = namee
        person['value'] = format(0, '.15g')
        return person
        
        
def initPerson4(person):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table1 = dynamodb.Table('FindLogic')
    namee = person['value']
    response = table1.get_item(Key={'name': namee})
    if 'Item' in response:
        person_db = response['Item']
        return person_db
    else:
        return -1
        
def solveLogicArithmeticRelativeLess(intent,session):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table1 = dynamodb.Table('FindLogic')
    card_title = 'Solve Logic Books'
    session_attributes = {}
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    person1 = intent['slots']['Main_User']
    person2 = intent['slots']['Secondary_User']
    quantity = intent['slots']['Quantity']['value']

    person_db1 = initPerson3(person1)
    person_db2 = initPerson4(person2)
    speech_output = "Ok. Noted. Next Statement?"
    if person_db1 == -1 or person_db2 == -1:
        return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          "Wrong Inputs", reprompt_text,
                          should_end_session))

    person_db1['value'] = float(person_db2['value'])-float(quantity)
    explain="Since, " + person_db1['name'] +' has ' + str(quantity) + ' less than ' + person_db2['name'] +'. So If ' + person_db2['name'] + ' has '+ str(int(person_db2['value'])) +' ' + intent['slots']['Things']['value'] + ' then as per the statement '+ person_db1['name'] + ' will have '+ str(int(person_db1['value']))  + ' ' + intent['slots']['Things']['value']  
    putTable1(person_db1)
    putTable3(explain)
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
                          
    
def solveLogicArithmeticQuestionName(intent, session):

    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table1 = dynamodb.Table('FindLogic')
    card_title = 'Solve Logic Statement'

    name1 = intent['slots']['Name']['value']
    response = table1.get_item(Key={'name': name1})

    print (response)
    if 'Item' in response:
        speech_output = str(name1)+" has "+str(response['Item']['value'])+" "+str(intent['slots']['Things']['value'])
    else:
        speech_output = 'Wrong Question!'

    session_attributes = {}
    explain=speech_output
    putTable3(explain)
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
                          
def solveLogicArithmeticQuestionTotal(intent, session):

    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table1 = dynamodb.Table('FindLogic')
    card_title = 'Explain logic Statement Total'

    result=table1.scan()
    count =0
    stri=''
    for i in range (0, result['Count']):
            stri = stri + str(int(result['Items'][i]['value'])) + '+ '
            count=float(count)+float(result['Items'][i]['value'])
    speech_output = "Total number of "+str((intent['slots']['Things']['value']))+" are "+str(count)
    session_attributes = {}
    explain = speech_output + ' ('+ stri+'0)'
    putTable3(explain)
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
                          
                    
#---------------------------------------------------------------------------------------------------#

def solveDirectionAbsoluteIntent(intent,session):
    session_attributes={}
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table2 = dynamodb.Table('Direction')
    result=table2.scan()
    count=result["Count"]
    if count == 0:
        person = {}
        person['x']=0
        person['y']=0
        person['snum']=0
        person['distancecovered']=0
        person['currdirection']='north'
        print ('hi')
        print (person)
        putTable2(person)
        
    card_title = 'Solve euclid'
    direction = intent['slots']['Direction_Absolute']
    units = intent['slots']['Units']['value']
    
    person_db = initDirection(direction,session, units)
    
    print (person_db)
    putTable2(person_db)
    explain='Moved by ' +  str( intent['slots']['Units']['value']) + ' units in ' + intent['slots']['Direction_Absolute']['value']
    putTable3(explain)
    speech_output = 'Ok. Next statement please.'
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
    
def initDirection(direction,session,units):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table2 = dynamodb.Table('Direction')
    result=table2.scan()
    count=result["Count"]
    direction=direction['value']
    session_attributes={}
    person_db={}
    units=float(units);
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table2 = dynamodb.Table('Direction')
    result=table2.scan()
    count=result["Count"]
    #if count == 0:
     #   session_attributes['prevx'] = format(float(0), '.15g')
      #  session_attributes['prevy'] = format(float(0), '.15g')
      # session_attributes['prevdistancecovered'] = format(float(0), '.15g')
    response = table2.get_item(Key={'snum': count})
    print(response)
    if 'Item' in response:
        print (session)
        #print (session_attributes)
        response=response['Item']
        person_db['distancecovered'] = float(response['distancecovered'])+ units
        #session['attributes']['prevdistancecovered'] = person_db['distancecovered']
        person_db['snum'] = count
        if direction == "north":
            person_db['y'] = float((response['y'])) + units
            person_db['x'] = response['x']
            person_db['currdirection'] = direction
        elif direction == "south":
            person_db['y'] = float(response['y']) - units
            person_db['x'] = response['x']
            person_db['currdirection'] = direction
        elif direction == "east":
            person_db['x'] = float(response['x']) + units
            person_db['y'] = response['y']
            person_db['currdirection'] = direction
        elif direction == "west":
            person_db['x'] = float(response['x']) - units
            person_db['y'] = response['y']
            person_db['currdirection'] = direction
        return person_db

def putTable2(person):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table2 = dynamodb.Table('Direction')
    result=table2.scan()
    c=result["Count"]
    c=c+1
    response = table2.get_item(Key={'snum': c})
    if 'Item' in response:
        table2.delete_item(Key={'snum': c})
    #print (person['currdirection'])
    print (person)
    table2.put_item(Item={'snum': c,'distancecovered': format(float(person['distancecovered']),'.15g'),'currdirection': person['currdirection'],'x':format(float(person['x']),'.15g'),'y': format(float(person['y']),'.15g')})
 
 
    
  
def solveDirectionRelativeIntent(intent,session):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table2 = dynamodb.Table('Direction')
    card_title = 'Solve euclid'
    direction = intent['slots']['Direction_Relative']['value']
    units = intent['slots']['Units']['value']
    person_db = initDirection1(direction,session, units)
    print (person_db)
    putTable2(person_db)
    speech_output = 'Ok. Next statement please.'
    session_attributes = {}
    explain='Moved by ' +  str( intent['slots']['Units']['value']) + ' units in ' + intent['slots']['Direction_Relative']['value']
    putTable3(explain)
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))

def initDirection1(direction,session, units):
    person_db={}
    session_attributes={}
    units=float(units);
    
    
    
    flag=0
    print (direction)
    if(direction == 'up' or direction == 'forward'):
        flag=0
    elif (direction == 'down' or direction == 'backward'):
        flag=2
    elif (direction == 'right'):
        flag=1
    elif(direction == 'left'):
        flag=3
    print (flag)
    Index=['north','east','south','west']
    
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table2 = dynamodb.Table('Direction')
    result=table2.scan()
    count=result["Count"]
    count = count +1
    response = table2.get_item(Key={'snum': count-1})
    print (response)
    for i in range(0,4):
        if (Index[i]==response['Item']['currdirection']):
            break;
    print (Index[i])
    direction=Index[(i+flag)%4]
    print (i,flag)
    print (direction)
    if 'Item' in response:
        print (session)
        #print (session_attributes)
        response=response['Item']
        person_db['distancecovered'] = float(response['distancecovered'])+ units
        #session['attributes']['prevdistancecovered'] = person_db['distancecovered']
        person_db['snum'] = count
        if direction == "north":
            person_db['y'] = float((response['y'])) + units
            person_db['x'] = response['x']
            person_db['currdirection'] = direction
        elif direction == "south":
            person_db['y'] = float(response['y']) - units
            person_db['x'] = response['x']
            person_db['currdirection'] = direction
        elif direction == "east":
            person_db['x'] = float(response['x']) + units
            person_db['y'] = response['y']
            person_db['currdirection'] = direction
        elif direction == "west":
            person_db['x'] = float(response['x']) - units
            person_db['y'] = response['y']
            person_db['currdirection'] = direction
    return person_db


def solveDirectionQuestionDistance(intent,session):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table2 = dynamodb.Table('Direction')
    card_title = 'Explain logic Statement Distance'
    result=table2.scan()
    count=result["Count"]
    p = table2.get_item(Key={'snum': count})
    p = p['Item']
    speech_output = "Total distance is "+str(int(p['distancecovered']))
    session_attributes = {}
    explain = speech_output
    putTable3(explain)
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))

def solveDirectionQuestionDisplacement(intent,session):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table2 = dynamodb.Table('Direction')
    card_title = 'Explain logic Statement Distance'
    result=table2.scan()
    count=result["Count"]
    p = table2.get_item(Key={'snum': count})
    p = p['Item']
    disp=sqrt(math.pow(float(p['x']),2) + math.pow(float(p['y']),2))
    speech_output = "Total displacement is "+str(disp)
    session_attributes = {}
    explain = speech_output
    putTable3(explain)
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
                          

def solveDirectionQuestionDirectionAbsolute(intent,session):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table2 = dynamodb.Table('Direction')
    card_title = 'Explain logic Statement Direction Absolute'
    result=table2.scan()
    count=result["Count"]
    p = table2.get_item(Key={'snum': count})
    p=p['Item']
    speech_output = "Current Direction is "+str(p["currdirection"])
    session_attributes = {}
    explain = speech_output
    putTable3(explain)
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
                          
                          
                          
def solveDirectionQuestionDirectionRelative(intent,session):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table2 = dynamodb.Table('Direction')
    card_title = 'Explain logic Statement Direction relative'
    result=table2.scan()
    count=result["Count"]
    p = table2.get_item(Key={'snum': count})
    p=p['Item']
    x = float(p['x'])
    y = float(p['y'])
    if(x==0 and y >0):
        result = 'north'
    elif(x==0 and y<0):
        result ='south'
    elif(y==0 and x>0):
        result ='east'
    elif(y==0 and x==0):
        result = 'Starting point'
    elif(x==y and x >0):
        result = 'North-East'
    elif(x==y and x<0):
        result = 'South-West'
    elif(x==-y and x>0):
        result= 'South-East'
    elif(x==-y and x<0):
        result ='North-west'
    else:
        result=str(math.atan(float(y)/float(x)))
        result = result + ' radians' 
    speech_output = "Relative Direction with respect to origin is "+ result ;
    session_attributes = {}
    explain = speech_output
    putTable3(explain)
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
                          


                          
                    
#---------------------------------------------------------------------------------------------------#

def AgeStatementAssignAbsolutePresent(intent,session):
    session_attributes={}
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table4 = dynamodb.Table('Age_Logic')
    card_title = 'Solve Age Absolute Present'
    Name = intent['slots']['Name']['value']
    Age = intent['slots']['Quantity']['value']
    person_db={}
    person_db['Name'] =Name 
    person_db['Age'] =Age
    print (person_db)
    putTable4(person_db)
    speech_output = 'Ok. Next statement please.'
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
                          

def putTable4(person):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table4 = dynamodb.Table('Age_Logic')
    #person['Name'] = person['Name'].encode('ascii', 'ignore')
    response = table4.get_item(Key={'Name': person['Name']})
    if 'Item' in response:
            table4.delete_item(
                Key={
                    'Name': person['Name']
                })
    table4.put_item(Item={'Age': format(float(person['Age']), '.15g'), 'Name': person['Name']})


def AgeStatementAssignYearAbsolute(intent,session):
    session_attributes={}
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table4 = dynamodb.Table('Age_Logic')
    card_title = 'Solve Age Year Absolute'
    Name = intent['slots']['Name']['value']
    Year = intent['slots']['Year']['value']
    person_db={}
    strings = time.strftime("%Y,%m,%d,%H,%M,%S")
    t = strings.split(',')
    numbers = [ int(x) for x in t ]
    #person['Name'] = person['Name'].encode('ascii', 'ignore')
    Year=int(Year.encode('ascii', 'ignore'))
    Age= numbers[0] - Year
    if(Age >= 0):
        person_db['Name'] =Name 
        person_db['Age'] =Age
        putTable4(person_db)
        speech_output = 'Ok. Next statement please.'
    else:
        speech_output = 'I cannot consider a person from future'
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
                          

def AgeStatementAssignAbsoluteFuture(intent,session):
    session_attributes={}
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table4 = dynamodb.Table('Age_Logic')
    card_title = 'Solve Age Absolute Future'
    Name = intent['slots']['Name']['value']
    Year = intent['slots']['Value_Future']['value']
    Quantity=intent['slots']['Quantity']['value']
    Quantity=int(Quantity.encode('ascii', 'ignore'))
    if ((Name is None) or (Year is None) or (Quantity is None)):
        speech_output = 'There is some issue with framing of sentence. kindly try again.'
        should_end_session = False
        reprompt_text = 'I almost heard it. Can you try again?'
        return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
                          
    if (Year == 'next' or Year == 'coming'):
        Year=1
    elif (Year == 'this'):
        Year=0
    else:
        Year=int(Year.encode('ascii', 'ignore'))
    Age=Quantity-Year
    person_db={}
    if(Age >= 0):
        person_db['Name'] =Name 
        person_db['Age'] =Age
        putTable4(person_db)
        speech_output = 'Ok. Next statement please.'
    else:
        speech_output = 'Logically incorrect statement. Kindly try again'
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
                          

def AgeStatementAssignAbsolutePast(intent,session):
    session_attributes={}
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table4 = dynamodb.Table('Age_Logic')
    card_title = 'Solve Age Absolute Past'
    Name = intent['slots']['Name']['value']
    Year = intent['slots']['Value_Past']['value']
    Quantity=intent['slots']['Quantity']['value']
    Quantity=int(Quantity.encode('ascii', 'ignore'))
    if ((Name is None) or (Year is None) or (Quantity is None)):
        speech_output = 'There is some issue with framing of sentence. kindly try again.'
        should_end_session = False
        reprompt_text = 'I almost heard it. Can you try again?'
        return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
                          
    if (Year == 'last' or Year == 'previous'):
        Year=1
    else:
        Year=int(Year.encode('ascii', 'ignore'))
    Age=Quantity+Year
    person_db={}
    if(Age >= 0):
        person_db['Name'] =Name 
        person_db['Age'] =Age
        putTable4(person_db)
        speech_output = 'Ok. Next statement please.'
    else:
        speech_output = 'Logically incorrect statement. Kindly try again'
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))

def AgeStatementAssignYearRelative(intent,session):
    session_attributes={}
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table4 = dynamodb.Table('Age_Logic')
    card_title = 'Solve Age Absolute Past'
    Name = intent['slots']['Name']['value']
    Year = intent['slots']['Year']['value']
    Quantity=intent['slots']['Quantity']['value']
    Quantity=int(Quantity.encode('ascii', 'ignore'))
    Year=int(Year.encode('ascii', 'ignore'))
    if ((Name is None) or (Year is None) or (Quantity is None)):
        speech_output = 'There is some issue with framing of sentence. kindly try again.'
        should_end_session = False
        reprompt_text = 'I almost heard it. Can you try again?'
        return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
                          
    strings = time.strftime("%Y,%m,%d,%H,%M,%S")
    t = strings.split(',')
    numbers = [ int(x) for x in t ]
    Age= numbers[0] - Year
    Age=Quantity+Age
    person_db={}
    if(Age >= 0):
        person_db['Name'] =Name 
        person_db['Age'] =Age
        putTable4(person_db)
        speech_output = 'Ok. Next statement please.'
    else:
        speech_output = 'Logically incorrect statement. Kindly try again'
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
                          
                          
def AgeAssignPresentMultipy(intent,session):
    session_attributes={}
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table4 = dynamodb.Table('Age_Logic')
    card_title = 'Solve Age Assign Present Multiply'
    First_User = intent['slots']['First_User']['value']
    Value= intent['slots']['Value_Multiply']['value']
    Second_User=intent['slots']['Second_User']['value']
    
    if ((First_User is None) or (Value is None) or (Second_User is None)):
        speech_output = 'There is some issue with framing of sentence. kindly try again.'
        should_end_session = False
        reprompt_text = 'I almost heard it. Can you try again?'
        return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
    person={}
    SecondUser=initPersonByAge(Second_User)
    FirstUser=initPersonByAge(First_User)
    if(Value=='twice'):
        Value=2
    elif(Value=='thrice'):
        Value=3
    elif(Value=='half' or Value=='Half'):
        Value=0.5
    else:
        Value=int(Value.encode('ascii', 'ignore'))
    
    if (('Age' not in SecondUser.keys()) and ('Age' not in FirstUser.keys())):
        speech_output = 'Logically incorrect statement. Kindly try again'
        should_end_session = False
        reprompt_text = 'I almost heard it. Can you try again?'
        return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
    if(('Age' in SecondUser.keys())):
        if ((SecondUser['Age'] is not None)):
            SecondUser['Age']=int(SecondUser['Age'].encode('ascii', 'ignore'))
            person['Name']=FirstUser['Name']
            Age= SecondUser['Age']*Value
            person['Age']=Age
    if(('Age' not in SecondUser.keys()) and (('Age' in FirstUser.keys()))):
        FirstUser['Age']=int(FirstUser['Age'].encode('ascii', 'ignore'))
        person['Name']=SecondUser['Name']
        Value=float(Value)
        Value=1/Value;
        Age= FirstUser['Age']*Value
        person['Age']=Age
    
    if(person['Age'] >= 0):
        putTable4(person)
        speech_output = 'Ok. Next statement please.'
    else:
        speech_output = 'Logically incorrect statement. Kindly try again'
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
                          
                          
def initPersonByAge(Name):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table4 = dynamodb.Table('Age_Logic')
    response = table4.get_item(Key={'Name': Name})
    person={}
    if 'Item' in response:
        person['Name'] = Name
        person['Age'] = response['Item']['Age']
        return person
    else:
        person['Name'] = Name
        return person


def AgeAssignPresentRelation(intent,session):
    session_attributes={}
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table4 = dynamodb.Table('Age_Logic')
    card_title = 'Solve Age Assign Present Multiply'
    First_User = intent['slots']['First_User']['value']
    Relation= intent['slots']['Relation']['value']
    Second_User=intent['slots']['Second_User']['value']
    Quantity= intent['slots']['Quantity']['value']
    Quantity=int(Quantity.encode('ascii', 'ignore'))
    
    if ((First_User is None) or (Second_User is None) or (Quantity is None) or (Relation is None) ):
        speech_output = 'There is some issue with framing of sentence. kindly try again.'
        should_end_session = False
        reprompt_text = 'I almost heard it. Can you try again?'
        return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
    person={}
    SecondUser=initPersonByAge(Second_User)
    FirstUser=initPersonByAge(First_User)
    
    if(Relation=='younger' or Relation=='smaller' or Relation=='less mature' or Relation=='less'):
        Quantity= -Quantity
    elif(Relation=='elder' or Relation=='mature' or Relation=='more' or Relation=='older'):
        Quantity=Quantity
    
    if (('Age' not in SecondUser.keys()) and ('Age' not in FirstUser.keys())):
        speech_output = 'Logically incorrect statement. Kindly try again'
        should_end_session = False
        reprompt_text = 'I almost heard it. Can you try again?'
        return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
    if(('Age' in SecondUser.keys())):
        if ((SecondUser['Age'] is not None)):
            SecondUser['Age']=int(SecondUser['Age'].encode('ascii', 'ignore'))
            person['Name']=FirstUser['Name']
            Age= SecondUser['Age']+Quantity
            person['Age']=Age
    if(('Age' not in SecondUser.keys()) and (('Age' in FirstUser.keys()))):
        FirstUser['Age']=int(FirstUser['Age'].encode('ascii', 'ignore'))
        person['Name']=SecondUser['Name']
        Age= FirstUser['Age']-Quantity
        person['Age']=Age
    
    if(person['Age'] >= 0):
        putTable4(person)
        speech_output = 'Ok. Next statement please.'
    else:
        speech_output = 'Logically incorrect statement. Kindly try again'
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))


def AgeAssignPastMultipy(intent,session):
    session_attributes={}
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table4 = dynamodb.Table('Age_Logic')
    card_title = 'Solve Age Assign Present Multiply'
    First_User = intent['slots']['First_User']['value']
    Value= intent['slots']['Value_Multiply']['value']
    Second_User=intent['slots']['Second_User']['value']
    Value_Past=intent['slots']['Value_Past']['value']
    
    if ((First_User is None) or (Value is None) or (Second_User is None)):
        speech_output = 'There is some issue with framing of sentence. kindly try again.'
        should_end_session = False
        reprompt_text = 'I almost heard it. Can you try again?'
        return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
    person={}
    SecondUser=initPersonByAge(Second_User)
    FirstUser=initPersonByAge(First_User)
    if(Value=='twice'):
        Value=2
    elif(Value=='thrice'):
        Value=3
    elif(Value=='Half'):
        Value=0.5
    else:
        Value=int(Value.encode('ascii', 'ignore'))
        
    if (Value_Past == 'last' or Value_Past == 'previous'):
        Value_Past=1
    else:
        Value_Past=int(Value_Past.encode('ascii', 'ignore'))
    
    if (('Age' not in SecondUser.keys()) and ('Age' not in FirstUser.keys())):
        speech_output = 'Logically incorrect statement. Kindly try again'
        should_end_session = False
        reprompt_text = 'I almost heard it. Can you try again?'
        return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
    if(('Age' in SecondUser.keys())):
        if ((SecondUser['Age'] is not None)):
            SecondUser['Age']=int(SecondUser['Age'].encode('ascii', 'ignore'))
            person['Name']=FirstUser['Name']
            Age= (SecondUser['Age']-Value_Past)*Value
            person['Age']=Age+Value_Past
    if(('Age' not in SecondUser.keys()) and (('Age' in FirstUser.keys()))):
        FirstUser['Age']=int(FirstUser['Age'].encode('ascii', 'ignore'))
        person['Name']=SecondUser['Name']
        Value=float(Value)
        Value=1/Value;
        Age= (FirstUser['Age']-Value_Past)*Value
        person['Age']=Age+Value_Past
    
    if(person['Age'] >= 0):
        putTable4(person)
        speech_output = 'Ok. Next statement please.'
    else:
        speech_output = 'Logically incorrect statement. Kindly try again'
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
    
    
    
def AgeAssignFutureMultipy(intent,session):
    session_attributes={}
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table4 = dynamodb.Table('Age_Logic')
    card_title = 'Solve Age Assign Present Multiply'
    First_User = intent['slots']['First_User']['value']
    Value= intent['slots']['Value_Multiply']['value']
    Second_User=intent['slots']['Second_User']['value']
    Value_Future=intent['slots']['Value_Future']['value']
    
    if ((First_User is None) or (Value is None) or (Second_User is None)):
        speech_output = 'There is some issue with framing of sentence. kindly try again.'
        should_end_session = False
        reprompt_text = 'I almost heard it. Can you try again?'
        return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
    person={}
    SecondUser=initPersonByAge(Second_User)
    FirstUser=initPersonByAge(First_User)
    if(Value=='twice'):
        Value=2
    elif(Value=='thrice'):
        Value=3
    elif(Value=='Half'):
        Value=0.5
    else:
        Value=int(Value.encode('ascii', 'ignore'))
        
    if (Value_Future == 'next' or Value_Future == 'coming'):
        Value_Future=1
    elif (Year == 'this'):
        Value_Future=0
    else:
        Value_Future=int(Value_Future.encode('ascii', 'ignore'))
    
    if (('Age' not in SecondUser.keys()) and ('Age' not in FirstUser.keys())):
        speech_output = 'Logically incorrect statement. Kindly try again'
        should_end_session = False
        reprompt_text = 'I almost heard it. Can you try again?'
        return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
    if(('Age' in SecondUser.keys())):
        if ((SecondUser['Age'] is not None)):
            SecondUser['Age']=int(SecondUser['Age'].encode('ascii', 'ignore'))
            person['Name']=FirstUser['Name']
            Age= (SecondUser['Age']+Value_Future)*Value
            person['Age']=Age-Value_Future
    if(('Age' not in SecondUser.keys()) and (('Age' in FirstUser.keys()))):
        FirstUser['Age']=int(FirstUser['Age'].encode('ascii', 'ignore'))
        person['Name']=SecondUser['Name']
        Value=float(Value)
        Value=1/Value;
        Age= (FirstUser['Age']+Value_Future)*Value
        person['Age']=Age-Value_Future
    
    if(person['Age'] >= 0):
        putTable4(person)
        speech_output = 'Ok. Next statement please.'
    else:
        speech_output = 'Logically incorrect statement. Kindly try again'
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
        

def AgeQuestionByName(intent,session):
    session_attributes={}
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table4 = dynamodb.Table('Age_Logic')
    card_title = 'Solve Age Question By Name'
    Name = intent['slots']['Name']['value']
    response = table4.get_item(Key={'Name': Name})
    person={}
    if 'Item' in response:
        person['Name'] = Name
        person['Age'] = response['Item']['Age']
        Answer='Age of ' + person['Name'] + ' is '  + str(person['Age'])
        speech_output = Answer
    else:
        speech_output = 'Not able to find any person by name ' + Name
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
                          
                          
def AgeQuestionByLowest(intent,session):
    session_attributes={}
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table4 = dynamodb.Table('Age_Logic')
    card_title = 'Solve Age Question By Lowest'
    person={}
    result=table4.scan()
    flag=0
    print ("-----------")
    print ()
    min =10000
    minloc =1000
    for i in range (0, result['Count']):
        if  float(result['Items'][i]['Age'])==min:
            flag=flag+1
            if(flag==1):
                Answer_Name = str(result['Items'][i]['Name']) +' and ' + str(Answer_Name)
            else:
                Answer_Name = str(result['Items'][i]['Name']) + ', ' + str(Answer_Name)
        if float(result['Items'][i]['Age'])<min:
            Answer_Name=(result['Items'][i]['Name'])
            Answer_Age = float(result['Items'][i]['Age'])
            min=float(result['Items'][i]['Age'])
            flag=0
            
    if (Answer_Age == int(Answer_Age)):
        Answer_Age=int(Answer_Age)
    else:
        Answer_Age=float(Answer_Age)
        
    if (result['Count'] == 0):
        speech_output = 'No value in the Database'
    else:
        if(flag == 0):
            speech_output = str(Answer_Name) + ' is the youngest with age ' + str(Answer_Age) + ' years'
        else:
            speech_output = str(Answer_Name) + ' are the youngest with age ' + str(Answer_Age) + ' years'
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))

 
def AgeQuestionByHighest(intent,session):
    session_attributes={}
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table4 = dynamodb.Table('Age_Logic')
    card_title = 'Solve Age Question By Highest'
    person={}
    result=table4.scan()
    flag=0
    max =-1
    for i in range (0, result['Count']):
        if  float(result['Items'][i]['Age'])==max:
            flag=flag+1
            if(flag==1):
                Answer_Name = str(result['Items'][i]['Name']) +' and ' + str(Answer_Name)
            else:
                Answer_Name = str(result['Items'][i]['Name']) + ', ' + str(Answer_Name)
        if float(result['Items'][i]['Age'])>max:
            Answer_Name=(result['Items'][i]['Name'])
            Answer_Age = float(result['Items'][i]['Age'])
            max=float(result['Items'][i]['Age'])
            flag=0
            
    if (Answer_Age == int(Answer_Age)):
        Answer_Age=int(Answer_Age)
    else:
        Answer_Age=float(Answer_Age)
        
    if (result['Count'] == 0):
        speech_output = 'No value in the Database'
    else:
        if(flag == 0):
            speech_output = str(Answer_Name) + ' is the eldest  with age ' + str(Answer_Age) + ' years'
        else:
            speech_output = str(Answer_Name) + ' are the eldest with age ' + str(Answer_Age) + ' years'
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))

def AgeQuestionByYear(intent,session):
    session_attributes={}
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table4 = dynamodb.Table('Age_Logic')
    card_title = 'Solve Age Question By Year'
    Name = intent['slots']['Name']['value']
    response = table4.get_item(Key={'Name': Name})
    person={}
    if 'Item' in response:
        person['Name'] = Name
        person['Age'] = response['Item']['Age']
        strings = time.strftime("%Y,%m,%d,%H,%M,%S")
        t = strings.split(',')
        numbers = [ int(x) for x in t ]
        Age= numbers[0] - float(person['Age'])
        if (Age == int(Age)):
            Age=int(Age)
        else:
            Age=float(Age)
        Answer=person['Name'] + ' was born in '  + str(Age)
        speech_output = Answer
    else:
        speech_output = 'Not able to find any person by name ' + Name
    should_end_session = False
    reprompt_text = 'I almost heard it. Can you try again?'
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                          speech_output, reprompt_text,
                          should_end_session))
    
    
    


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please tell me your favorite color by saying, " \
                    "my favorite color is red."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Alexa Skills Kit sample. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def create_favorite_color_attributes(favorite_color):
    return {"favoriteColor": favorite_color}


def set_color_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'Color' in intent['slots']:
        favorite_color = intent['slots']['Color']['value']
        session_attributes = create_favorite_color_attributes(favorite_color)
        speech_output = "I now know your favorite color is " + \
                        favorite_color + \
                        ". You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
        reprompt_text = "You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your favorite color is. " \
                        "You can tell me your favorite color by saying, " \
                        "my favorite color is red."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_color_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "You can say, my favorite color is red."
        should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == 'Logic_Solve_Start':
        return solveLogicStart(intent, session)
    elif intent_name == 'Logic_Solve_End':
        return solveLogicStatementEnd(intent, session)
    elif intent_name == 'Logic_Arthimetic_Statement_Simple':
        return solveLogicArithmetic(intent, session)
    elif intent_name == 'Logic_Arthimetic_Statement_Exchange':
        return solveLogicArithmeticExchange(intent, session)
    elif intent_name == 'Logic_Arthimetic_Statement_Relative_More':
        return solveLogicArithmeticRelativeMore(intent, session)
    elif intent_name == 'Logic_Arthimetic_Statement_Relative_Less':
        return solveLogicArithmeticRelativeLess(intent, session)
    elif intent_name == 'Logic_Arthimetic_Question_By_Name':
        return solveLogicArithmeticQuestionName(intent, session)
    elif intent_name == 'Logic_Arthimetic_Question_Thing_All':
        return solveLogicArithmeticQuestionTotal(intent, session)
    elif intent_name == 'Direction_Absolute_intent':
        return solveDirectionAbsoluteIntent(intent,session)
    elif intent_name == 'Direction_Relative_intent':
        return solveDirectionRelativeIntent(intent,session)
    elif intent_name == 'Direction_Question_Distance':
        return solveDirectionQuestionDistance(intent,session)
    elif intent_name == 'Direction_Question_Displacement':
        return solveDirectionQuestionDisplacement(intent,session)
    elif intent_name == 'Direction_Question_Direction_Absolute':
        return solveDirectionQuestionDirectionAbsolute(intent,session)
    elif intent_name == 'Direction_Question_Direction_Relative':
        return solveDirectionQuestionDirectionRelative(intent,session)
    elif intent_name == 'Age_Statement_Assign_Absolute_Present':
        return AgeStatementAssignAbsolutePresent(intent,session)
    elif intent_name == 'Age_Statement_Assign_Absolute_Past':
        return AgeStatementAssignAbsolutePast(intent,session)
    elif intent_name == 'Age_Statement_Assign_Year_Relative':
        return AgeStatementAssignYearRelative(intent,session)
    elif intent_name == 'Age_Assign_Present_Multipy':
        return AgeAssignPresentMultipy(intent,session)
    elif intent_name == 'Age_Statement_Assign_Absolute_Future':
        return AgeStatementAssignAbsoluteFuture(intent,session)
    elif intent_name == 'Age_Statement_Assign_Year_Absolute':
        return AgeStatementAssignYearAbsolute(intent,session)
    elif intent_name == 'Age_Assign_Present_Relation':
        return AgeAssignPresentRelation(intent,session)
    elif intent_name == 'Age_Assign_Past_Multipy':
        return AgeAssignPastMultipy(intent,session)
    elif intent_name == 'Age_Assign_Future_Multipy':
        return AgeAssignFutureMultipy(intent,session)
    elif intent_name == 'Age_Assign_Past_Relation':
        return AgeAssignPresentRelation(intent,session)
    elif intent_name == ' Age_Assign_Future_Relation':
        return AgeAssignPresentRelation(intent,session)
    elif intent_name == 'Age_Question_By_Name':
        return AgeQuestionByName(intent,session)
    elif intent_name == 'Age_Question_By_Lowest':
        return AgeQuestionByLowest(intent,session)
    elif intent_name == 'Age_Question_By_Highest':
        return AgeQuestionByHighest(intent,session)
    elif intent_name == 'Age_Question_By_Year':
        return AgeQuestionByYear(intent,session)
    elif intent_name == 'AMAZON.HelpIntent':
        return get_welcome_response()
    elif intent_name == 'AMAZON.CancelIntent' or intent_name == 'AMAZON.StopIntent':
        return handle_session_end_request()
    else:
        raise ValueError('Invalid intent')

def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
