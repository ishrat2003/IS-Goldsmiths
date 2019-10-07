import nltk
import re
import pprint
import random
import json
import pprint


class Markov(object):
	def __init__(self, order=2, dictFile="", maxWordInSentence=20, fileEncoding="utf-8"):
		self.table = {}
		self.inputLineCount = 0
		self.inputWordCount = 0
		self.setOrder( order )
		self.setMaxWordInSentence(maxWordInSentence)
		if dictFile:
			self.loadDictionary(dictFile, fileEncoding)


	def setOrder(self, order=2):
		self.order = order

	def loadDictionary(self, dictFile, fileEncoding="utf-8"):
		print("Loaded dictionary file: " + dictFile)
		with open(dictFile, 'r', encoding=fileEncoding) as inf:
			self.table = eval(inf.read())

		# pprint.pprint(self.table)

	def readFile(self, filename, fileEncoding="utf-8"):
		with  open(filename, "r", encoding=fileEncoding) as file:
			strLine = " ".join(file)
			self.processSection(strLine)

	def processSection(self,line ):
		#print('---------------------------------')
		# global lineCount, wordCount, table, keyLen
		sent_text = nltk.sent_tokenize(line) # this gives us a list of sentences

		for sentence in sent_text:
			self.inputLineCount = self.inputLineCount  + 1

			tokens = sentence.split()
			keyList = [ ];

			#Add a special key with just beginning words
			self.table.setdefault( '#BEGIN#', []).append(tokens[0:self.order ]);

			#loop through each word, and if we have enough to add dictionary item, then add
			for item in tokens:
				
				#item = self.__clean(item)

				if len(keyList) < self.order :  #not enough items
					keyList.append(item)
					continue

				#If we already have the item, then add it, otherwise add to empty list
				self.table.setdefault( tuple(keyList), []).append(item)

				#Remove the first word and push last word on to it
				keyList.pop(0)
				keyList.append(item)
				self.inputWordCount = self.inputWordCount + 1

		#print(self.table)
		return

	def setMaxWordInSentence(self, maxWordInSentence):
		self.maxWordInSentence = maxWordInSentence

	def genText(self):	
		key = list(random.choice(self.table['#BEGIN#']))

		genStr = " ".join( key )
		for _ in range( self.maxWordInSentence ):
			#print('---------------------')
			#print('key: ', key)
			#print(tuple(key))
			newKey = self.table.setdefault( tuple(key), None) 
			if(not newKey):
				break

			#print('new key: ', newKey)
			newVal = random.choice( newKey )
			#print('new val: ', newVal)
			genStr = genStr + " " + newVal

			key.pop(0)
			key.append(newVal)

		return genStr

	def getLineCount(self):
		return self.inputLineCount

	def getWordCount(self):
		return self.inputWordCount

	def outputDict(self, filename, fileEncoding="utf-8"):
		with open(filename, 'w', encoding=fileEncoding) as file:
			pprint.pprint(self.table, file)
		#pprint.pprint(self.table,markovDictFile)

	def __clean(self, text):
		text = re.sub('<.+?>', '. ', text)
		text = re.sub('&.+?;', '', text)
		text = re.sub('[\']{1}', '', text)
		text = re.sub('[^a-zA-Z0-9\s_\-\?:;\.,!\(\)\"]+', ' ', text)
		text = re.sub('\s+', ' ', text)
		text = re.sub('(\.\s*)+', '. ', text)
		return text
