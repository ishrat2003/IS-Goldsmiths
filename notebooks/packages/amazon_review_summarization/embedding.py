import numpy as np
import sys

class Embedding():

    def __init__(self, initialEmbeddingFilePath, vocab, outputFilePath):
        self.initialEmbeddingFilePath = initialEmbeddingFilePath
        self.outputFilePath = outputFilePath
        self.vocab = vocab
        self.embeddingsIndex = {}
        return

    def load(self):
        self.embeddingsIndex = {}
        with open(self.initialEmbeddingFilePath + 'numberbatch-en-17.06.txt', encoding='utf-8') as file:
            for line in file:
                values = line.split(' ')
                word = values[0]
                embedding = np.asarray(values[1:], dtype='float32')
                self.embeddingsIndex[word] = embedding

        print('Word embeddings length:', len(self.embeddingsIndex))
        print('Word embeddings shape:', self.embeddingsIndex[word].shape)
        return


    def missingWords(self):
        missingWords = 0
        threshold = 20
        print('Missing words:')
        for word, count in self.vocab.items():
            if count > threshold:
                if word not in self.embeddingsIndex:
                    missingWords += 1
                    print(word)
            
        missingRatio = round(missingWords/len(self.vocab),4)*100
            
        print("Number of words missing from CN:", missingWords)
        print("Percent of words that are missing from vocabulary: {}%".format(missingRatio))
        return