# Developed by: Kishwar KUMAR
# Email: kumar.kishwar@gmail.com

# Description:
#
# Software Used: PyCharm (Community License)
# Operating System: OSX

from ReadData import ReadCSV
import statsmodels.formula.api as sm
import patsy
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import classification_report
class LogisticRegression1:

    # Define constructor
    def __init__(self, Path):
        self.path = Path
        return

    def ModelLogisticReg(self):
        print '+++++++++++++++++++++++++ LOGISTIC REGRESSION 1 +++++++++++++++++++++++++'

        # Read csv file.. First get handle
        comLRHandle = ReadCSV.Read_CSV()
        data = comLRHandle.Read(self.path)

        # Let count the data and check if any missing info/value
        #print data.count(0)

        #PassengerId    891
        #Survived       891
        #Pclass         891
        #Name           891
        #Sex            891
        #Age            714
        #SibSp          891
        #Parch          891
        #Ticket         891
        #Fare           891
        #Cabin          204
        #Embarked       889

        # We need to remove Name, Cabin and Ticket because these are not useful
        data = data.drop(['Ticket', 'Cabin', 'Name'], axis=1)

        # Drop Na also.. We may fill them with avg/some other method.. but lets drop for now
        data = data.dropna()

        #We'll use a Python package called Patsy, which helps in describing statistical models.
        #It helps in defining a dependent and independent variable formula that is similar to
        #R. The variable that is defined left of '~' is the dependent variable, and the variable
        #that is defined to right of it are the independent variables. The variables enclosed
        #within C() are treated as categorical variables.

        formula = 'Survived ~ C(Pclass) + C(Sex) + Age + SibSp + C(Embarked) + Parch'

        # Lets create a dictionary to hold regression result for easy analysis
        DFTdataX = data.iloc[0: 600, : ]   # take first 600 samples (For Training)
        DFVdataX = data.iloc[600: , : ]    # take remaining samples (For Testing)

        # Splitting the data into dependent and independent variables
        TdataY, TdataX = patsy.dmatrices(formula, data=DFTdataX, return_type='dataframe')
        VdataY, VdataX = patsy.dmatrices(formula, data=DFVdataX, return_type='dataframe')

        # Let instantiate out model using stats package
        LogistModel = sm.Logit(TdataY, TdataX)

        # Execute model to let it fit
        ResLogModel = LogistModel.fit()

        #print ResLogModel.summary()

                                   #Logit Regression Results
        #==============================================================================
        #Dep. Variable:               Survived   No. Observations:                  600
        #Model:                          Logit   Df Residuals:                      591
        #Method:                           MLE   Df Model:                            8
        #Date:                Fri, 13 Nov 2015   Pseudo R-squ.:                  0.3333
        #Time:                        22:39:44   Log-Likelihood:                -270.02
        #converged:                       True   LL-Null:                       -404.99
                                        #LLR p-value:                 1.009e-53
        #====================================================================================
        #                       coef    std err          z      P>|z|      [95.0% Conf. Int.]
        #------------------------------------------------------------------------------------
        #-Intercept            4.3332      0.510      8.490      0.000         3.333     5.334
        #-C(Pclass)[T.2]      -1.2030      0.325     -3.703      0.000        -1.840    -0.566
        #-C(Pclass)[T.3]      -2.4673      0.320     -7.705      0.000        -3.095    -1.840
        #-C(Sex)[T.male]      -2.6312      0.244    -10.797      0.000        -3.109    -2.154
        #+C(Embarked)[T.Q]    -0.4359      0.647     -0.674      0.501        -1.704     0.832
        #+C(Embarked)[T.S]    -0.2910      0.297     -0.980      0.327        -0.873     0.291
        #-Age                 -0.0397      0.009     -4.464      0.000        -0.057    -0.022
        #-SibSp               -0.3202      0.136     -2.354      0.019        -0.587    -0.054
        #+Parch               -0.1420      0.136     -1.041      0.298        -0.409     0.125
        #====================================================================================
        # As we can see Psudo R-Squ.=0.333, it is good.. any error between 0.2-0.4 is OK
        # As we can see also Embarktion and Parch has P>0.050 these people don't have much
        # significance over predication. Well, we offcourse want few predictors, let re-design
        # our formula and see what happens

        # Lets update formula again.. removing Embarked and Parch
        formula = 'Survived ~ C(Pclass) + C(Sex) + Age + SibSp '

        # Splitting the data into dependent and independent variables
        TdataY, TdataX = patsy.dmatrices(formula, data=DFTdataX, return_type='dataframe')
        VdataY, VdataX = patsy.dmatrices(formula, data=DFVdataX, return_type='dataframe')

        # Let instantiate out model using stats package
        LogistModel = sm.Logit(TdataY, TdataX)

        # Execute model to let it fit
        ResLogModel = LogistModel.fit()

        #print ResLogModel.summary()

                                  #Logit Regression Results
        #==============================================================================
        #Dep. Variable:               Survived   No. Observations:                  600
        #Model:                          Logit   Df Residuals:                      594
        #Method:                           MLE   Df Model:                            5
        #Date:                Sun, 15 Nov 2015   Pseudo R-squ.:                  0.3307
        #Time:                        12:26:13   Log-Likelihood:                -271.08
        #converged:                       True   LL-Null:                       -404.99
        #                                        LLR p-value:                 8.172e-56
        #==================================================================================
        #                     coef    std err          z      P>|z|      [95.0% Conf. Int.]
        #----------------------------------------------------------------------------------
        #-Intercept          4.1050      0.479      8.575      0.000         3.167     5.043
        #-C(Pclass)[T.2]    -1.2971      0.306     -4.242      0.000        -1.896    -0.698
        #-C(Pclass)[T.3]    -2.5739      0.305     -8.433      0.000        -3.172    -1.976
        #-C(Sex)[T.male]    -2.5808      0.235    -10.996      0.000        -3.041    -2.121
        #-Age               -0.0401      0.009     -4.549      0.000        -0.057    -0.023
        #-SibSp             -0.3691      0.130     -2.840      0.005        -0.624    -0.114
        #==================================================================================
        # We can see that all the predictors are significant in the preceding model.

        # Let evaluate the model and see how good it works with validation/testing data

        # We will use Kernel Density Estimation
        kde_res = sm.nonparametric.KDEUnivariate(ResLogModel.predict())
        kde_res.fit()
        #plt.plot(kde_res.support,kde_res.density)
        #plt.fill_between(kde_res.support,kde_res.density, alpha=0.2)
        #plt.title("Distribution of our Predictions")
        #plt.show()
        # From image we can see most of the distribution (highest density) is over 0. That means
        # most of the people had died. This is true in case of titanic dataset.

        # Let's see the prediction distribution based on the male gender:
        #plt.scatter(ResLogModel.predict(),TdataX['C(Sex)[T.male]'] , alpha=0.2)
        #plt.grid(b=True, which='major', axis='x')
        #plt.xlabel("Predicted chance of survival")
        #plt.ylabel("Male Gender")
        #plt.title("The Change of Survival Probability by Gender being Male")
        #plt.show()
        # As we can see from image, probability of survival is high for female compare to male.

        # Now, let's see the distribution of the prediction based on the lower class of the passengers:
        #plt.scatter(ResLogModel.predict(),TdataX['C(Pclass)[T.3]'] , alpha=0.2)
        #plt.xlabel("Predicted chance of survival")
        #plt.ylabel("Class Bool") # Boolean class to show if its 3rd class
        #plt.grid(b=True, which='major', axis='x')
        #plt.title("The Change of Survival Probability by Lower Class which is 3rd class")
        #plt.show()
        # We can see from image, lower class people has lower chance of survival compare to uper class.
        # More money can save you...

        # Let's see the distribution of the probability with respect to the age of the passengers:
        #plt.scatter(ResLogModel.predict(),TdataX.Age , alpha=0.2)
        #plt.grid(True, linewidth=0.15)
        #plt.title("The Change of Survival Probability by Age")
        #plt.xlabel("Predicted chance of survival")
        #plt.ylabel("Age")
        #plt.show()
        # If we see the graph. There are two outcomes...
        # 1. Small children of age around 0-1 year has predicted chance of survival spread over full range.
        # 2. As the age increase, chance of survival go to left of graph which is less chance of survival.
        # but this graph is distribution over wide range of Age unlike above 2 graphs (binary).

        # Let's see the distribution of the probability with respect to the number of siblings/spouses:
        #plt.scatter(ResLogModel.predict(),TdataX.SibSp , alpha=0.2)
        #plt.grid(True, linewidth=0.15)
        #plt.title("The Change of Survival Probability by Number of siblings/spouses")
        #plt.xlabel("Predicted chance of survival")
        #plt.ylabel("No. of Siblings/Spouses")
        #plt.show()
        # Less the family member on board.. more the chances of survival.

        ## Evaluating a model based on test data ##
        y_pred = ResLogModel.predict(VdataX)
        y_pred_flag = y_pred > 0.7
        print '------------------------------------------------------------------------------------------'
        print pd.crosstab(VdataY.Survived, y_pred_flag, rownames = ['Actual'], colnames = ['Predicted'])
        print '------------------------------------------------------------------------------------------'
        print classification_report(VdataY, y_pred_flag)
        print '------------------------------------------------------------------------------------------'