from . import Base

class Display(Base):

    def __init__(self, inputFile, show = True):
        super().__init__(inputFile, show)
        return


    def showReviews(self, number = 5):
        for i in range(number):
            print("Review #", i+1)
            print(self.reviews.Summary[i])
            print(self.reviews.Text[i])
            print("---------------------------------------")
        return
    