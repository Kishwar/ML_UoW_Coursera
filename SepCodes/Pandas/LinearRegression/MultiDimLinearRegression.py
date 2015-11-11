# Developed by: Kishwar KUMAR
# Date: 11/nov/2015
# Email: kumar.kishwar@gmail.com

# Description: In this file, we will try to implement Mult-Dimension linear regression model on two dimensional
#               data (Height and Weight). We will try to fit our model with given data (Mens_height_weight.csv).
# Software Used: PyCharm (Community License)
# Operating System: OSX

from ReadData import ReadCSV
import matplotlib.pyplot as plt
from sklearn import linear_model,cross_validation, feature_selection, preprocessing
import statsmodels.formula.api as sm
from statsmodels.tools.eval_measures import mse
from statsmodels.tools.tools import add_constant
from sklearn.metrics import mean_squared_error

class MultiDimLinearRegression1:

    # Define constructor
    def __init__(self, Path):
        self.path = Path
        return

    def ModelLinearRegression1(self):
        print '+++++++++++++++++++++++++ MULTI-DIM LINEAR REGRESSION 1 +++++++++++++++++++++++++'

        # Read csv file.. First get handle
        comLRHandle = ReadCSV.Read_CSV()
        data = comLRHandle.Read(self.path)

        # Lets print data and some maths
        print data
        print data.describe()

        # As we can see data is multi-Dimensional (more than 2 dim). We need to find something
        # which help us to use Linear Regression on this Multi-Dim data.
        # Lets print correlation Matrix to get some info..
        print '---------------------------- CORRELATION MATRIX ---------------------------- '
        print data.corr()
        print '-----------------------------------------------------------------------------'

        # Lets plot data to have visual info
        #fig, ax = plt.subplots(1,1)
        #ax.scatter(data.height, data.avg_points_scored)
        #ax.set_xlabel('height')
        #ax.set_ylabel('Average points scored per game')
        #plt.show()
        #fig, ax = plt.subplots(1,1)
        #ax.scatter(data.weight, data.avg_points_scored)
        #ax.set_xlabel('weight')
        #ax.set_ylabel('Average points scored per game')
        #plt.show()
        #fig, ax = plt.subplots(1,1)
        #ax.scatter(data.success_field_goals, data.avg_points_scored)
        #ax.set_xlabel('success_field_goals')
        #ax.set_ylabel('Average points scored per game')
        #plt.show()
        #fig, ax = plt.subplots(1,1)
        #ax.scatter(data.success_free_throws, data.avg_points_scored)
        #ax.set_xlabel('success_free_throws')
        #ax.set_ylabel('Average points scored per game')
        #plt.show()

        # This is highly deviated data against avg_points_scored. It will be difficult for the model
        # to analyze and predict. Let see what happens..

        # Lets break data in 2 pieces (training data (80%) and test data (20%))
        dataX = data.values.copy()
        TdataX, VdataX, TdataY, VdataY = cross_validation.train_test_split(dataX[:,:-1],
                                                                           dataX[:, -1],
                                                                           train_size= 0.80)

        # Lets use Ordinary Least Square (OLS) regression
        ols = sm.OLS(TdataY, add_constant(TdataX)).fit()
        print ols.summary()
