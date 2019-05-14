from .markov import Markov
from nltk.stem.porter import PorterStemmer
import re
import sys

class CWR(Markov):


    def __init__(self, order=2, dictFile="", maxWordInSentence=20, fileEncoding="utf-8"):
        super().__init__(order, dictFile, maxWordInSentence, fileEncoding)
        self.contributors = []
        self.stemmer = PorterStemmer()
        self.titles = []
        return


    def setContributors(self, contributors):
        self.contributors = contributors
        return

    def getTitles(self):
        starters = self.__getStarters()
        self.titles = []

        for starter in starters:
            title = [word for word in starter]
            self.__buildTitle(starter, title)
            
 
        #print(self.titles)
		
        return self.titles[0:3]


    def __buildTitle(self, state, title = []):
        if len(title) > self.maxWordInSentence:
            # Too big for title
            return False

        words = self.__getNextWords(state)
        lastWord = title[-1]
        if not words or (lastWord[-1] in ['.', ',', ';']):
            titleString = " ".join(title)
            if lastWord[-1] in ['.', ',', ';']:
                titleString = titleString[0:-1]
            self.titles.append(titleString)
            #print('-------------------')
            #print(" ".join(title))
            return True


        processedWords = []
        words = words[0:2]

        for word in words:
            if word in processedWords:
                continue
            appendedTitle = title + [word]
            #print('appendedTitle: ', appendedTitle)
            #print('title: ', title)

            nextState = [item for item in state]
            nextState.pop(0)
            nextState.append(word)
            #print('nextState: ', nextState)

            if (len(appendedTitle) > self.maxWordInSentence):
                # Too long
                break

            self.__buildTitle(nextState, appendedTitle)
            processedWords.append(word)
            
        return True


    def __getNextWords(self, state):
        return self.table.setdefault(tuple(state), None)



    def __getStarters(self):
        starters = self.table['#BEGIN#']
        if not starters:
            return []

        initiators = []
        scores = []
        maxScore = 0

        for starter in starters:
            stemmedStarter = [self.__clean(self.stemmer.stem(word.lower())) for word in starter]
            matched = [item for item in stemmedStarter if item in self.contributors] 
            score = len(matched)
            if score > 0:
                initiators.append(starter)
                scores.append(score)
                if score > maxScore :
                    maxScore = score

        finalStarters = []
        index = 0
        for starter in initiators:
            if scores[index] == maxScore:
                finalStarters.append(starter)

            index += 1

        return finalStarters


    def __clean(self, text):
        text = re.sub('<.+?>', '. ', text)
        text = re.sub('&.+?;', '', text)
        text = re.sub('[\']{1}', '', text)
        text = re.sub('[^a-zA-Z0-9\s_\-\?:;\.,!\(\)\"]+', ' ', text)
        text = re.sub('\s+', ' ', text)
        text = re.sub('(\.\s*)+', '. ', text)
        return text

