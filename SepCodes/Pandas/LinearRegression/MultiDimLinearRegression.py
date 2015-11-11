# Developed by: Kishwar KUMAR
# Date: 11/nov/2015
# Email: kumar.kishwar@gmail.com

# Description: In this file, we will try to implement Mult-Dimension linear regression model on two dimensional
#               data (Height and Weight). We will try to fit our model with given data (Mens_height_weight.csv).
# Software Used: PyCharm (Community License)
# Operating System: OSX

from ReadData import ReadCSV

class MultiDimLinearRegression1:

    # Define constructor
    def __init__(self):
        return

    def ModelLinearRegression1(self):
        print '+++++++++++++++++++++++++ MULTI-DIM LINEAR REGRESSION 1 +++++++++++++++++++++++++'

        # Read csv file.. First get handle
        comLRHandle = ReadCSV.Read_CSV()
        data = comLRHandle.Read('Data/basketball.csv')