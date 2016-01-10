# These are my assignment project codes developed in python.
# Anyone can use these codes without any permission
# Assessing Fit (polynomial regression)
#
# Contact info: Kishwar Kumar [kumar.kishwar@gmail.com]
# Country: France
#



__author__ = 'kishwarkumar'
__date__ = '10/1/16' '8:33 PM'

# imports
from sklearn import linear_model
import numpy as np
from Common import Common

class PolynomialRegression:

    # Define constructor
    def __init__(self):
        return

    # Entry method
    def callme(self):
        print "++++++++++++++++++++++ Regression Week 3: Polynomial Regression ++++++++++++++++++++++"
        cmnHandle = Common()
        df_train = cmnHandle.readcsv("../data/kc_house_train_data.csv")
        df_test = cmnHandle.readcsv("../data/kc_house_test_data.csv")

        tmp = np.array(range(3))
        print cmnHandle.polynomial_sframe(tmp, 3)

        poly1_data = cmnHandle.polynomial_sframe(df_train['sqft_living'], 1)

        print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"