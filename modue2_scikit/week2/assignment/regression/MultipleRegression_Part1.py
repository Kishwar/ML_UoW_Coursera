# These are my assignment project codes developed in python.
# Anyone can use these codes without any permission
#
# Contact info: Kishwar Kumar [kumar.kishwar@gmail.com]
# Country: France
#

__author__ = 'kishwarkumar'
__date__ = '6/1/16' '10:07 PM'

# imports
import pandas as pd

class MultipleRegression_Part1:

    # Define constructor
    def __init__(self):
        return

    # Function reads CSV and retuns dataframe
    def ReadCSV(self, path):
        return pd.read_csv(path)

    # Extract feature from DataFrame and generate new DataFrame
    def Extract(self, DFInput, Features):
        df1 = pd.DataFrame(DFInput[Features[1]])
        df2 = pd.DataFrame(DFInput[Features[0]])
        dflistv= [df1, df2]
        DFRetrun = pd.concat(dflistv)
        loopIndex = 0
        for feature in Features:
            if loopIndex == 0:
                loopIndex += 1
                continue
            DFRetrun = DFRetrun + DFInput[feature]
        DFRetrun = pd.DataFrame(DFRetrun, columns=Features)
        return DFRetrun


    # Entry method
    def CallMe(self):
        DFTrain = self.ReadCSV("../data/kc_house_train_data.csv")
        DFTest = self.ReadCSV("../data/kc_house_test_data.csv")
        example_features = ['sqft_living', 'bedrooms', 'bathrooms']
        DFUpdated = self.Extract(DFTrain, example_features)
