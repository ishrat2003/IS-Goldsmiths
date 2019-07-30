from . import Base 
import pandas as pd

class Indexify():

    def __init__(self, vocabIndex):
        self.vocabIndex = vocabIndex
        self.wordCount = 0
        self.unkCount = 0
        return

    def process(self, fieldPath, fieldName):
        print(fieldPath)
        indexifiedTexts = []
        self.wordCount = 0
        self.unkCount = 0
        for text in pd.read_csv(fieldPath):
            print('---------------------')
            print(text)
            indexifiedTexts.append(self.convertToIndexes(text, True))
        print('???????????????????????', len(indexifiedTexts))
        path = fieldPath[:-4]  + '_indexify.csv'
        dataFrame = pd.DataFrame(indexifiedTexts)
        dataFrame.to_csv(path, sep='\t', encoding='utf-8', index=False, header=False)
        print("%s indexifying finished." % (fieldName))

        unkPercent = round(self.unkCount/self.wordCount,4)*100
        print("Total number of words in ", fieldName, ":", self.wordCount)
        print("Total number of UNKs in  ", fieldName, ":", self.unkCount)
        print("Percent of words that are UNK: {}%".format(unkPercent))
        return path

    def convertToIndexes(self, text, eos=False):
        '''Convert words in text to an integer.
        If word is not in vocab_to_int, use UNK's integer.
        Total the number of words and UNKs.
        Add EOS token to the end of texts'''
        ints = []
        for sentence in text:
            sentenceInts = []
            for word in sentence.split():
                self.wordCount += 1
                if word in self.vocabIndex:
                    sentenceInts.append(self.vocabIndex[word])
                else:
                    sentenceInts.append(self.vocabIndex["<UNK>"])
                    self.unkCount += 1
                
            if eos:
                sentenceInts.append(self.vocabIndex["<EOS>"])
            ints.append(sentenceInts)
        
        return ints
    