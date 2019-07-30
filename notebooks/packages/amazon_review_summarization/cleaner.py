import re
import pandas as pd
from nltk.corpus import stopwords
from . import Base

class Cleaner(Base):

    def __init__(self, inputFile, outputFilePath, show):
        super().__init__(inputFile, show)
        self.__loadContractions()
        self.outputFilePath = outputFilePath
        return


    def saveClean(self, fieldName, removeContractions = True, removeStopwords = True):
        cleanTexts = []
        for text in getattr(self.reviews, fieldName):
            cleanTexts.append(self.cleanText(text, removeContractions, removeStopwords))

        path = self.outputFilePath + fieldName + '.csv'

        dataFrame = pd.DataFrame(cleanTexts)
        dataFrame.to_csv(path, sep='\t', encoding='utf-8', index=False, header=False)
        print("%s cleaning finished." % (fieldName))
        return path


    def cleanText(self, text, removeContractions = True, removeStopwords = True):
        '''Remove unwanted characters, stopwords, and format the text to create fewer nulls word embeddings'''

        # Convert words to lower case
        text = text.lower()

        # Replace contractions with their longer forms 
        if removeContractions:
            text = self.__removeContractions(text)

            # Format words and remove unwanted characters
            text = self.__format(text)

        # Optionally, remove stop words
        if removeStopwords:
            text = self.__removeStopwords(text)

        return text

    def __removeContractions(self, text):
        # We are not using "text.split()" here
        #since it is not fool proof, e.g. words followed by punctuations "Are you kidding?I think you aren't."
        text = re.findall(r"[\w']+", text)
        new_text = []
        for word in text:
            if word in self.contractions:
                new_text.append(self.contractions[word])
            else:
                new_text.append(word)

        text = " ".join(new_text)
        return text

    def __format(self, text):
        text = re.sub(r'https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)# remove links
        text = re.sub(r'\<a href', ' ', text)# remove html link tag
        text = re.sub(r'&amp;', '', text) 
        text = re.sub(r'[_"\-;%()|+&=*%.,!?:#$@\[\]/]', ' ', text)
        text = re.sub(r'<br />', ' ', text)
        text = re.sub(r'\'', ' ', text)
        return text

    def __removeStopwords(self, text):
        text = text.split()
        stops = set(stopwords.words("english"))
        text = [w for w in text if not w in stops]
        text = " ".join(text)
        return text

    def __loadContractions(self):
        self.contractions = { 
            "ain't": "am not",
            "aren't": "are not",
            "can't": "cannot",
            "can't've": "cannot have",
            "'cause": "because",
            "could've": "could have",
            "couldn't": "could not",
            "couldn't've": "could not have",
            "didn't": "did not",
            "doesn't": "does not",
            "don't": "do not",
            "hadn't": "had not",
            "hadn't've": "had not have",
            "hasn't": "has not",
            "haven't": "have not",
            "he'd": "he would",
            "he'd've": "he would have",
            "he'll": "he will",
            "he's": "he is",
            "how'd": "how did",
            "how'll": "how will",
            "how's": "how is",
            "i'd": "i would",
            "i'll": "i will",
            "i'm": "i am",
            "i've": "i have",
            "isn't": "is not",
            "it'd": "it would",
            "it'll": "it will",
            "it's": "it is",
            "let's": "let us",
            "ma'am": "madam",
            "mayn't": "may not",
            "might've": "might have",
            "mightn't": "might not",
            "must've": "must have",
            "mustn't": "must not",
            "needn't": "need not",
            "oughtn't": "ought not",
            "shan't": "shall not",
            "sha'n't": "shall not",
            "she'd": "she would",
            "she'll": "she will",
            "she's": "she is",
            "should've": "should have",
            "shouldn't": "should not",
            "that'd": "that would",
            "that's": "that is",
            "there'd": "there had",
            "there's": "there is",
            "they'd": "they would",
            "they'll": "they will",
            "they're": "they are",
            "they've": "they have",
            "wasn't": "was not",
            "we'd": "we would",
            "we'll": "we will",
            "we're": "we are",
            "we've": "we have",
            "weren't": "were not",
            "what'll": "what will",
            "what're": "what are",
            "what's": "what is",
            "what've": "what have",
            "where'd": "where did",
            "where's": "where is",
            "who'll": "who will",
            "who's": "who is",
            "won't": "will not",
            "wouldn't": "would not",
            "you'd": "you would",
            "you'll": "you will",
            "you're": "you are"
            }
        return