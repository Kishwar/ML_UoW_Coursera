# These codes are developed using book "Mastering Python for Data Science.pdf"
# Developed by: Kishwar KUMAR
# Date: 11/nov/2015
# Email: kumar.kishwar@gmail.com
# Software Used: PyCharm (Community License)
# Operating System: OSX

from DirectoryChange import ChangeDirectoryPath
from LinearRegression import LinearRegression1

__author__ = 'kishwarkumar'
__date__ = '11/11/15' '4:51 PM'

if __name__ == "__main__":

    # Get Handle and Change Path
    DrChange = ChangeDirectoryPath.ChangeDir()
    DrChange.SetDir('/Users/kishwarkumar/Documents/MachineLearningCourse_UOfWashington/SepCodes/Pandas')
    DrChange.ChangeIt()

    # Get Handle for LinearRegression1
    LR1 = LinearRegression1.LinearRegression1()
    LR1.ModelLinearRegression1()