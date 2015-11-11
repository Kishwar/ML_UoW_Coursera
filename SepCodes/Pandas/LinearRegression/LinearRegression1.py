# These codes are developed using book "Mastering Python for Data Science.pdf"
# Developed by: Kishwar KUMAR
# Date: 11/nov/2015
# Email: kumar.kishwar@gmail.com

# Description: In this file, we will try to implement linear regression model on two dimensional data
#              (Height and Weight). We will try to fit our model with given data (Mens_height_weight.csv).
# Software Used: PyCharm (Community License)
# Operating System: OSX

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

class LinearRegression1:


# Read csv data file
data = pd.read_csv('Data/Mens_height_weight.csv')

# Let plot it
fig, ax = plt.subplots(1, 1)
ax.scatter(data['Height'], data['Weight'])
plt.show()

class CommonLinearRegression:
    def ReadCSV(self, Path):
        return