from . import Dataset
import utility
import os
import json
import datetime

class Brexit(Dataset):


    def __init__(self, path):
        super().__init__(path, 'brexit')
        return


    def read(self, fileName):
        identifier = fileName[:-8]
        #print('identifier:', identifier)
        details = super().read(fileName)
        if not details:
            return details

        filePath = os.path.join(self.datasetPath, (identifier + '.json'))
        fileHandler = utility.File(filePath)
        otherDetails = fileHandler.read()
        if otherDetails:
                otherDetails = json.loads(otherDetails)
                details['url'] = otherDetails['Url']
                details['categories'] = otherDetails['Categories']
                if 'Title' in otherDetails.keys():
                    details['title'] = self._clean(otherDetails['Title'])
                    details['text'] = self._clean(otherDetails['Title']) + '. ' + details['text']

                if 'Date' in otherDetails.keys():
                    details['date'] = otherDetails['Date']
                    details['timestamp'] = int(datetime.datetime.strptime(otherDetails['Date'], '%Y-%m-%d').strftime("%s"))

        return details


    def print(self):
        self.resetFileIndex()
        details = self.getNextTextBlockDetails('all')
        while details:
            print('"' + details['title'] + '","' + details['date'] + '","' + details['categories'] + '","' + details['url'] + '"')
            details = self.getNextTextBlockDetails()
        
        return

