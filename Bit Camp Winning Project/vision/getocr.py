from datetime import datetime
from summarizer import summarize
import dateutil.parser
import time
import json
import sys
import requests

def performOCR():
	subscription_key = "290030e36ceb429fa4d1e478ba76fead"
	# print image_url, "https://image.ibb.co/jdwtKx/Whats_App_Image_2018_04_06_at_9_32_00_PM.jpg"
	
	# TEST
	image_url = "https://s3.amazonaws.com/bitbucket18/uploads/documentVision.jpg"
	
	# LIVE
	# image_url = "https://s3.amazonaws.com/bitbucket18/uploads/documentshot.jpg"
	print image_url
	headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
	#--base params
	#params   = {'visualFeatures': 'Categories,Description,Color'}

	#--ocr params
	params   = {'language': 'unk', 'detectOrientation ': 'true'}
	data     = {'url': image_url}

	#analysis base url
	vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"

	ocr_url = vision_base_url + "ocr"
	vision_analyze_url = vision_base_url + "analyze"

	response = requests.post(ocr_url, headers=headers, params=params, json=data)
	response.raise_for_status()
	analysis = response.json()
	output = {}
	text=""
	for region in analysis["regions"]:
		for line in region["lines"]:
			for word in line["words"]:
				text=text+word["text"]+" "

	# getting text summary
	title="Title"
	summary=summarize(title, text)
	summary = ''.join(summary)

	# print text
	pattern = '%Y-%m-%d %H:%M:%S'
	currtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	

	epoch = dateutil.parser.parse(currtime).strftime('%s')

	# epoch = int(time.mktime(time.strptime(currtime, pattern)))
	# print epoch
	# print int(time.mktime(time.strptime(currtime, pattern)))
	ldakeyws = find_keyword(text)
	output['_id']=ldakeyws[0][0]
	output['time']=epoch
	output['text']=text
	output['summary']=''.join(summary)
	output['ldakeyws']=ldakeyws
	output = json.dumps(output)
	rp = requests.post('https://webhooks.mongodb-stitch.com/api/client/v2.0/app/devilseye-vlwxv/service/postArticle/incoming_webhook/webhook0?secret=ishan', data = output)

	return output


def find_keyword(test_string = 'We are from ASU and love going to hackathons'):
	key_file = open('words.txt')
	data = key_file.read()
	words = data.split()
	word_freq = {}
	for word in words:
	    if word in word_freq:
		word_freq[word]+=1
	    else:
		word_freq[word] = 1
	word_prob_dict = {}
	size_corpus = len(words)
	for word in word_freq:
	    word_prob_dict[word] = float(word_freq[word])/size_corpus

	prob_list = []
	for word, prob in word_prob_dict.items():
	     prob_list.append(prob)
	non_exist_prob = min(prob_list)/2

	words = test_string.split()
	test_word_freq = {}
	for word in words:
	    if word in test_word_freq:
		test_word_freq[word]+=1
	    else:
		test_word_freq[word] = 1

	test_words_ba = {}
	for word, freq in test_word_freq.items():
	    if word in word_prob_dict:
		test_words_ba[word] = freq/word_prob_dict[word]
	    else:
		test_words_ba[word] = freq/non_exist_prob

	test_word_ba_list = []
	for word, ba in test_words_ba.items():
	     test_word_ba_list.append((word, ba))

	def sort_func(a, b):
	    if a[1] > b[1]:
	       return -1
	    elif a[1] < b[1]:
		return 1
	    return 0

	test_word_ba_list.sort(sort_func)
	return test_word_ba_list[:2]

# performOCR()

