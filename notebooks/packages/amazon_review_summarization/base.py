import pandas as pd

class Base():

    def __init__(self, inputFile, show = False):
        self.show = show
        self.inputFile = inputFile
        self.loadReviews()
        return

    def loadReviews(self):
        self.reviews = pd.read_csv(self.inputFile)
        
        self.showReviewInfo()
        # Remove null values and unneeded features
        self.reviews = self.reviews.dropna()
        self.reviews = self.reviews.drop(['Id','ProductId','UserId','ProfileName','HelpfulnessNumerator','HelpfulnessDenominator',
                                'Score','Time'], 1)
        self.reviews = self.reviews.reset_index(drop=True)
        
        self.showReviewInfo()
        return self.reviews

    
    def showReviewInfo(self):
        if not self.show:
            return

        print("Input shape:")
        print(self.reviews.shape)
        print("Input head:")
        print(self.reviews.head())
        print("Null value information:")
        print(self.reviews.isnull().sum())
        print("---------------------------------------")
        print("---------------------------------------")
        return