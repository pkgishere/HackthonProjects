import nltk
from nltk.corpus import wordnet as wn

def createSimilarSentences(line):
	text = nltk.word_tokenize(line)
	list = nltk.pos_tag(text)
	verbs=[]
	reply = []
	for i in list:
		if(i[1]=="VB"):
			verbs.append(i[0])
	
		reply=[]
		reply.append(line)
		for i in verbs:
			Set=set()
			list=wn.synsets(i)
			for j in list:
				#print j.lemmas()
				listing= [str(lemma.name()) for lemma in j.lemmas()]
				for k in listing:
					Set.add(k)

			for l in Set:
				a=line.replace(i,l)
				reply.append(a)

		# print(reply)
	return reply
