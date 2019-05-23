import pandas as pd
import pickle

class Vocab():

    def __init__(self, filePaths, outputFilePath):
        self.vocab = {}
        self.filePaths = filePaths
        self.outputFilePath = outputFilePath
        return


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
        return


    def addToVocab(self, text):
        for sentence in text:
            for word in sentence.split():
                if word not in self.vocab.keys():
                    self.vocab[word] = 0
                self.vocab[word] += 1

        return
    
def count_words(count_dict, text):
    for sentence in text:
        for word in sentence.split():
            if word not in count_dict:
                count_dict[word] = 1
            else:
                count_dict[word] += 1