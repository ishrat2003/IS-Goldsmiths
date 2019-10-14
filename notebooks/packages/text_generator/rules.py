import nltk
import re
import pprint
import random
import json
import pprint
from nltk import word_tokenize, pos_tag

class Rules(object):

	def __init__(self):
		self.start = 'START'
		self.end = 'END'
		self.puntuation = 'PUNTUATION'
		self.rules = {}
		self.table = {}
		self.tableValues = {}
		self.terminals = {}
		self.columns = []
		self.maxLength = 0
		return

	def processFile(self, filename, fileEncoding="utf-8"):
		with open(filename, "r", encoding=fileEncoding) as file:
			fileContent = " ".join(file)
			self.process(fileContent)

		return

	def getRuleText(self, state = None, totalIncluded = 0):
		if state == self.end:
			return ''

		if not state:
			state = self.start

		score = 0
		text = ''
		if len(self.table[state]):
			text = ' '.join([text, state])
			totalIncluded += 1
			if totalIncluded <= self.maxLength:
				state =  random.choice(list(self.table[state].keys()))
				text += self.getRuleText(state)
		return text

	def process(self, line):
		line = self.__clean(line)
		sentences = nltk.sent_tokenize(line)
		
		self.columns.append(self.start)
		for sentence in sentences:
			types = []
			tokens = word_tokenize(sentence)
			tags = pos_tag(tokens)
			if self.maxLength < len(tags):
				self.maxLength = len(tags)

			for (word, type) in tags:
				# if len(type) == 1:
				# 	type = self.puntuation
				types.append(type)
				if type not in self.terminals.keys():
					self.terminals[type] = []

				if word not in self.terminals[type]:
					self.terminals[type].append(word)

			types.append(self.end)
			print(types)
			row = self.start
			if row not in self.table.keys():
				self.table[row] = {}

			for type in types:
				if type not in self.columns:
					self.columns.append(type)
					self.table[type] = {}
				if type not in self.table[row]:
					self.table[row][type] = 1
				else:
					self.table[row][type] += 1
				row = type


		print('------')
		print(self.columns)
		for row in self.table:
			self.tableValues[row] = []
			for column in self.columns:
				if column in self.table[row].keys():
					self.tableValues[row].append(1)
				else:
					self.tableValues[row].append(0)
			print(self.tableValues[row])

		print(self.table)
		print(self.terminals)
		print('Max length: ', self.maxLength)
		return


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
