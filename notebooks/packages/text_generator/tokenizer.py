from .core import Core
from nltk import word_tokenize, pos_tag

class Tokenizer(Core):

    def __init__(self, loggingLevel = None):
        super().__init__(loggingLevel)
        return

    def processTokens(self, text = None):
        if not text or not len(text):
            return

        self.tokens = word_tokenize(text)
        self.tags = pos_tag(self.tokens)
        self.updateMaxLength(self.tags)
 
        self.beforeProcessingTokens()
        for (word, type) in self.tags:
            self.updateTypes(type)
            self.updateTerminals(word, type)
            self.processToken(word, type)

        self.afterProcessingTokens()  
        return

    def beforeProcessingTokens(self):
        pass
        return

    def afterProcessingTokens(self):
        pass
        return

    def processToken(self, word, type):
        pass
        return

    def updateMaxLength(self, items):
        length = len(items)
        if length > self.maxLength:
            self.maxLength = length
        return

    def updateTerminals(self, word, type):
        if type not in self.terminals.keys():
            self.terminals[type] = []
        
        if word in self.terminals[type]:
            return

        self.terminals[type].append(word)
        return

    def updateTypes(self, type):
        if type in self.types:
            return
        self.types.append(type)
        return

    def _reset(self):
        self.maxLength = 0
        self.types = []
        self.terminals = {}
        self.tokens = []
        self.tags = []
        return

    def __clean(self, text):
        text = re.sub('<.+?>', '. ', text)
        text = re.sub('&.+?;', '', text)
        text = re.sub('[\']{1}', '', text)
        text = re.sub('[^a-zA-Z0-9\s_\-\?:;\.,!\(\)\"]+', ' ', text)
        text = re.sub('\s+', ' ', text)
        text = re.sub('(\.\s*)+', '. ', text)
        return text
	