from .tokenizer import Tokenizer
import pprint
import random

class PosType(Tokenizer):

    def __init__(self, order = 3, loggingLevel = None):
        super().__init__(loggingLevel)
        self.order = order
        return

    def train(self, fileName, fileEncoding="utf8"):
        self.logger.debug("Processing all titles.")
        self._reset()
        with open(fileName, "r+", encoding=fileEncoding) as file:
            self.logger.debug("File - " + fileName)
            for line in file:
                self.processTokens(line)

        return

    def load(self, dictFile, fileEncoding="utf8"):
        print("Loaded dictionary file: " + dictFile)
        with open(dictFile, 'r', encoding=fileEncoding) as inf:
            self.markovTable = eval(inf.read())
        return
    
    def save(self, filename, fileEncoding="utf-8"):
        with open(filename, 'w', encoding=fileEncoding) as file:
            pprint.pprint(self.markovTable, file)

        return

    def genRule(self, maxTerms = 15):	
        key = list(random.choice(self.markovTable['#BEGIN#']))

        genStr = " ".join(key)
        for _ in range(maxTerms):
            newKey = self.markovTable.setdefault(tuple(key), None) 
            if(not newKey):
                break

            newVal = random.choice(newKey)
            genStr = genStr + " " + newVal

            key.pop(0)
            key.append(newVal)

        return genStr

    def beforeProcessingTokens(self):
        self.keyList = []
        types = [type for (word, type) in self.tags]
        if '#BEGIN#' not in self.markovTable.keys():
            self.markovTable['#BEGIN#'] = []
        
        if types[0:self.order] not in self.markovTable['#BEGIN#']:
            self.markovTable['#BEGIN#'].append(types[0:self.order])
        
        return

    def afterProcessingTokens(self):
        self.totalTitles += 1
        return

    def processToken(self, word, type):
        if len(self.keyList) < self.order :  #not enough items
            self.keyList.append(type)
            return

        if tuple(self.keyList) not in self.markovTable.keys():
            self.markovTable[tuple(self.keyList)] = []
        
        if type not in self.markovTable[tuple(self.keyList)]:
            self.markovTable[tuple(self.keyList)].append(type)

        self.keyList.pop(0)
        self.keyList.append(type)
        return

    def _reset(self):
        self.markovTable = {}
        self.totalTitles = 0
        self.keyList = []
        super()._reset()
        return