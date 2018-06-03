import requests
import json
import base64

def text_reg():
    with open("data/test.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    url = 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyC5iYfo4yO76hFGBv9pSSXNrW4YQ3CG4V8'
    payload = {
  "requests":[
        {
          "image":{

              "content": encoded_string

          },
          "features":[
            {
              "type":"TEXT_DETECTION",
              "maxResults":1
            }
          ]
        }
      ]
    }

    headers = {'content-type': 'application/json'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    data = response.json()
    #print data
    #print data['responses'][0].keys()
    if 'textAnnotations' in data['responses'][0].keys():
        return data['responses'][0]['textAnnotations'][0]['description']
    else:
        return 'No text found'

def facial_emotion():

  with open("data/test.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

  url = 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyC5iYfo4yO76hFGBv9pSSXNrW4YQ3CG4V8'
  payload = {
    "requests":[
      {
        "image":{

            "content": encoded_string

        },
        "features":[
          {
            "type":"FACE_DETECTION",
            "maxResults":1
          }
        ]
      }
    ]
  }

  headers = {'content-type': 'application/json'}

  response = requests.post(url, data=json.dumps(payload), headers=headers)

  data = response.json()

  if 'faceAnnotations' in data['responses'][0]:
    if data['responses'][0]['faceAnnotations'][0]['joyLikelihood'] == 'VERY_LIKELY':
      print "Feeling happy"
    elif data['responses'][0]['faceAnnotations'][0]['sorrowLikelihood'] == 'VERY_LIKELY':
      print "Feeling sad"
    elif data['responses'][0]['faceAnnotations'][0]['surpriseLikelihood'] == 'VERY_LIKELY':
     print "Feeling surprise"
    elif data['responses'][0]['faceAnnotations'][0]['angerLikelihood'] == 'VERY_LIKELY':
      print "Feeling angry"
    else:
      print "Feeling neutral"
  else:
    print "No emotion detected"

def label_surroundings():
    with open("data/test.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    url = 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyC5iYfo4yO76hFGBv9pSSXNrW4YQ3CG4V8'
    payload = {
  "requests":[
        {
          "image":{

              "content": encoded_string

          },
          "features":[
            {
              "type":"LABEL_DETECTION",
            }
          ]
        }
      ]
    }

    headers = {'content-type': 'application/json'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    data = response.json()
    #print data
    #print data['responses'][0].keys()
    if 'labelAnnotations' in data['responses'][0].keys():
        list = [item['description'] for item in data['responses'][0]['labelAnnotations']]
        return list
    else:
        return "Nothing"

    

    #return data['responses'][0]['textAnnotations'][0]['description']







