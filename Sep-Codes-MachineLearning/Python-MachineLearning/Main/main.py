# Developed by: Kishwar KUMAR
# Email: kumar.kishwar@gmail.com
# Software Used: PyCharm (Community License)
# Operating System: OSX

from DirectoryChange import ChangeDirectoryPath
from LinearRegression import LinearRegression1
from LinearRegression import MultiDimLinearRegression
from LogisticRegression import LogisticRegression1

__author__ = 'kishwarkumar'

if __name__ == "__main__":

    # Get Handle and Change Path
    DrChange = ChangeDirectoryPath.ChangeDir()
    DrChange.SetDir('/Users/kishwarkumar/Documents/MachineLearningCourse_UOfWashington/SepCodes/Pandas')
    DrChange.ChangeIt()

    # Get handle for LinearRegression1
    #LR1 = LinearRegression1.LinearRegression1('Data/Mens_height_weight.csv')
    #LR1.ModelLinearRegression1()

    # Get handle for MultiDimLinearRegression
    #MDLR1 = MultiDimLinearRegression.MultiDimLinearRegression1('Data/basketball.csv')
    #MDLR1.ModelLinearRegression1()

    # Get handle for Logistic Regression
    LogReg = LogisticRegression1.LogisticRegression1('Data/titanic_data.csv')
    LogReg.ModelLogisticReg()