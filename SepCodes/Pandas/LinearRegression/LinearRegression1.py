# Developed by: Kishwar KUMAR
# Date: 11/nov/2015
# Email: kumar.kishwar@gmail.com

# Description: In this file, we will try to implement linear regression model on two dimensional data
#              (Height and Weight). We will try to fit our model with given data (Mens_height_weight.csv).
# Software Used: PyCharm (Community License)
# Operating System: OSX

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import datetime
from ReadData import ReadCSV

class LinearRegression1:

    # Define constructor
    def __init__(self, Path):
        self.path = Path
        return

    def ModelLinearRegression1(self):
        print '+++++++++++++++++++++++++ LINEAR REGRESSION 1 +++++++++++++++++++++++++'

        # Read csv file.. First get handle
        comLRHandle = ReadCSV.Read_CSV()
        data = comLRHandle.Read(self.path)

        # Print data and some maths
        print data
        print data.describe()

        # Plot Data
        #fig, ax = plt.subplots(1,1)
        #ax.set_xlabel('Height')
        #ax.set_ylabel('Weight')
        #ax.scatter(data['Height'], data['Weight'])
        #plt.show()

        print '---- CORRELATION MATRIX ----'
        print data.corr()
        print '----------------------------'

        # Start bench time
        print datetime.datetime.now().time()

        # Lets get Linear Regression Model Handle
        lm = linear_model.LinearRegression()

        # Train the system to fit for Min/least possible error
        lm.fit(data.Height[:, np.newaxis], data.Weight)

        print 'Weight Vector W = [' + str(lm.intercept_) + " " + str(lm.coef_) + ']'

        # End bench time
        print datetime.datetime.now().time()

        print pd.DataFrame(zip(data.columns,lm.coef_),
            columns = ['features', 'estimatedCoefficients'])

        print "If we write the equation: Weight = " + str(lm.coef_) + "Height + "  + str(lm.intercept_)

        # This is least fit model to this data. Model has tried to draw two dimension line with least
        # error between points and line. As Line is linear, there is still sufficient error between
        # points and line. This is very basic of all the models.
        # System can be verified by providing random Height to above equation and equation will
        # return Weight. See following example.
        print "What will be Weight when Height is 160"
        print "Weight = " + str(lm.coef_ * 160 + lm.intercept_)

        # We are not concerned about units (Kg/Pounds/meters/cm)

        # Lets Plot
        #fig, ax = plt.subplots(1,1)
        #ax.set_xlabel('Height')
        #ax.set_ylabel('Weight')
        #ax.scatter(data.Height,data.Weight)

        ###weight is the dependent variable and the height is the independent variable
        #ax.plot(data.Height,lm.predict(data.Height[:, np.newaxis]),
        #        color = 'red')
        #plt.show()
