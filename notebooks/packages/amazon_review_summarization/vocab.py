import pandas as pd
import pickle
import operator
import os

class Vocab():

    def __init__(self, outputFilePath, filePaths =[]):
        self.vocab = {}
        self.filePaths = filePaths
        self.outputFilePath = outputFilePath
        self.codes = ["<UNK>", "<PAD>", "<EOS>", "<GO>"] 
        return

    def loadVocab(self, number = 1000):
        path = self.outputFilePath + "vocab.pickle"
        if not os.path.exists(path):
            print('No vocab.pickle file found to load')
            return None
        vocab = pickle.load(open(path, "rb"))
        self.vocab = dict(sorted(vocab.items(), key = operator.itemgetter(1), reverse=True)[:number])

        usageRatio = round(len(self.vocab) / len(vocab), 4) * 100
        print("Total number of unique words:", len(vocab))
        print("Number of words we will use:", len(self.vocab))
        print("Percent of words we will use: {}%".format(usageRatio))
        return self.vocab

    def getVocabToIndex(self):
        vocabToIndex = {}

        for word in self.vocab.keys():
            vocabToIndex[word] = len(vocabToIndex)

        for code in self.codes:
            vocabToIndex[code] = len(vocabToIndex)

        return vocabToIndex

    def processVocab(self):
        for filePath in self.filePaths:
            dataFrame = pd.read_csv(filePath)
            for (index, text) in dataFrame.iterrows():
                self.addToVocab(text)
            
        print("Size of Vocabulary:", len(self.vocab))
        path = self.outputFilePath + "vocab.pickle"
        pickleFile = open(path, "wb")
        pickle.dump(self.vocab, pickleFile)
        pickleFile.close()
        return self.vocab

    def addToVocab(self, text):
        for sentence in text:
            for word in sentence.split():
                if word not in self.vocab.keys():
                    self.vocab[word] = 0
                self.vocab[word] += 1
        return
    
