import nltk
import re
import pprint
import random
import json
import pprint
from nltk import word_tokenize, pos_tag

class Grammer(object):
	def __init__(self, dictFile="", fileEncoding="utf-8"):
		self.table = {}
		self.setMaxWordInSentence(20)
		self.startSymbol = 'START'
		self.terminals = []
		#if dictFile:
		#	self.loadDictionary(dictFile, fileEncoding)
	
	def setMaxWordInSentence(self, maxWordInSentence):
		self.maxWordInSentence = maxWordInSentence

	def loadDictionary(self, dictFile, fileEncoding="utf-8"):
		with open(dictFile, 'r', encoding=fileEncoding) as inf:
			self.table = eval(inf.read())

	def readFile(self, filename, fileEncoding="utf-8"):
		with  open(filename, "r", encoding=fileEncoding) as file:
			strLine = " ".join(file)
			self.processSection(strLine)

	def processSection(self, line):
		line = self.__clean(line)
		sent_text = nltk.sent_tokenize(line) # this gives us a list of sentences

		for sentence in sent_text:
			tokens = word_tokenize(sentence)
			tags = pos_tag(tokens)
			types = [type for (word, type) in tags]
			print('---------------------')
			print(types)
			for (word, type) in tags:
				if len(type) == 1:
					continue
				tableKeys = self.table.keys()
				if type not in tableKeys:
					self.table[type] = []

				word = '"' + word + '"'
				if (word not in self.table[type]):
					self.table[type].append(word)
			
			
			lastIndex = self.startSymbol
			for type in types:
				if len(type) == 1:
					continue
					
				if (lastIndex not in self.table.keys()):
					self.table[lastIndex] = []

				if (type not in self.table[lastIndex]):
					self.table[lastIndex].append(type)

				lastIndex = type

		return

	

	def genGrammer(self):	
		rules = []
		for left in self.table.keys():
			rule = left + ' -> ' + ' | '.join(self.table[left])
			if rule not in rules:
				rules.append(rule)

		return "\n".join(rules)

	def outputDict(self, filename, fileEncoding="utf-8"):
		with open(filename, 'w', encoding=fileEncoding) as file:
			pprint.pprint(self.table, file)
		
	def __clean(self, text):
		text = text.replace("\n", ".")
		text = re.sub('<.+?>', '. ', text)
		text = re.sub('&.+?;', '', text)
		text = re.sub('[\']{1}', '', text)
		text = re.sub('[^a-zA-Z0-9\s_\-\?:;\.,!\(\)\"]+', ' ', text)
		text = re.sub('\s+', ' ', text)
		text = re.sub('(\.+\s*)+', '. ', text)
		text = re.sub(r'([\?|\!])\.', r'\1', text)
		return text
