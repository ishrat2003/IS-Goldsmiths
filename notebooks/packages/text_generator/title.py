from .tokenizer import Tokenizer
from lc.peripheral import Peripheral
import operator
import os
import nltk

class Title(Tokenizer):

    def __init__(self, loggingLevel = None):
        super().__init__(loggingLevel)
        return

    def train(self, fileName, fileEncoding="utf-8"):
        self.logger.debug("Processing all titles.")
        
        with open(fileName, "r", encoding=fileEncoding) as file:
            self.logger.debug("File - " + fileName)
            for line in file:
                self.processTokens(line)

        return

    def getTitle(self, text, limit = 10):
        peripheralProcessor = Peripheral()
        peripheralProcessor.setAllowedPosTypes(None)
        peripheralProcessor.setPositionContributingFactor(0.5)
        peripheralProcessor.setOccuranceContributingFactor(1)
        peripheralProcessor.setProperNounContributingFactor(0)
        peripheralProcessor.loadSentences(text)
        peripheralProcessor.train()
        wordInfo = peripheralProcessor.getWordInfo()

        sortedWords = sorted(wordInfo.values(), key=operator.itemgetter('score'), reverse=True)
        #featuredWords = [word for word in sortedWords]

        featuredWords = [word for word in sortedWords if word['type'] in ['NN', 'NNP', 'NNS', 'NNPS', 'JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS', 'VB']]
        print(featuredWords[0:limit])
        contributors = [word['pure_word'] for word in featuredWords[0:limit]]
        types = [word['type'] for word in featuredWords[0:limit]]
        print(contributors)
        print(types)
        self.markov(text)

        for contributor in contributors:
            contributor = contributor.lower()
            print('----------', contributor, '--------')
            if contributor in self.nextStates.keys():
                print(self.nextStates[contributor])
        #print(self.nextStates)
        return


    def getTerminals(self, sortedWords, limit = 10):
        terminals = {}
        for word in sortedWords:
            if word['type'] not in terminals.keys():
                terminals[word['type']] = []
            if word['pure_word'] not in terminals[word['type']]:
                terminals[word['type']].append(word['pure_word'])
        for wordType in terminals.keys():
            terminals[wordType] = terminals[wordType][0:limit]

        return terminals

    def beforeProcessingTokens(self):
        self.currentPosition = 0
        self.previousType = self.start
        self.previousWord = self.start
        return

    def afterProcessingTokens(self):
        self.totalTitles += 1
        return

    def processToken(self, word, type):
        # self.updatePositionVsPreviousType(self.currentPosition, self.previousType, type)
        # self.updatePositionCurrentCount(self.currentPosition, type)
        self.updateNextState(word, type)
        self.currentPosition += 1
        self.previousType = type
        return

    def updateNextState(self, word, type):
        word = word.lower()
        if self.previousWord not in self.nextStates.keys():
            self.nextStates[self.previousWord] = []

        if word not in self.nextStates[self.previousWord]:
            self.nextStates[self.previousWord].append(word)

        self.previousWord = word
        return

    def updatePositionCurrentCount(self, currentPosition, currentType):
        if currentPosition not in self.positionCurrentCount.keys():
            self.positionCurrentCount[currentPosition] = {}

        if currentType not in self.positionCurrentCount[currentPosition].keys():
            self.positionCurrentCount[currentPosition][currentType] = 1
        else :
             self.positionCurrentCount[currentPosition][currentType] += 1
        return

    def updatePositionVsPreviousType(self, position, previousType, currentType):
        if position not in self.positionVsPreviousType.keys():
            self.positionVsPreviousType[position] = {}

        if previousType not in self.positionVsPreviousType[position].keys():
            self.positionVsPreviousType[position][previousType] = []

        if currentType not in self.positionVsPreviousType[position][previousType]:
            self.positionVsPreviousType[position][previousType].append(currentType)
        return

    def markov(self, text, order = 2):
        self.table = {}
        sent_text = nltk.sent_tokenize(text) # this gives us a list of sentences

        for sentence in sent_text:
            tokens = sentence.split()
            keyList = []

            #Add a special key with just beginning words
            self.table.setdefault( '#BEGIN#', []).append(tokens[0:order])

            #loop through each word, and if we have enough to add dictionary item, then add
            for item in tokens:
                if len(keyList) < order :  #not enough items
                    keyList.append(item)
                    continue

                #If we already have the item, then add it, otherwise add to empty list
                self.table.setdefault(tuple(keyList), []).append(item)

                #Remove the first word and push last word on to it
                keyList.pop(0)
                keyList.append(item)

        print(self.table)
        return

    def _reset(self):
        self.start = 'start'
        self.totalTitles = 0
        self.positionVsPreviousType = {}
        self.positionCurrentCount = {}
        self.nextStates = {}
        super()._reset()
        return

	