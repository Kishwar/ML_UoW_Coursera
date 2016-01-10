# These are my assignment project codes developed in python.
# Anyone can use these codes without any permission
# Regression Week 2: Multiple Regression (gradient descent)
#
# Contact info: Kishwar Kumar [kumar.kishwar@gmail.com]
# Country: France
#

__author__ = 'kishwarkumar'
__date__ = '10/1/16' '6:35 PM'

# imports
import numpy as np
from math import sqrt
from common import Common

class MultipleRegressionPart2:

    # Define constructor
    def __init__(self):
        return

    # see notes
    def predict_output(self, feature_matrix, weights):
        # assume feature_matrix is a numpy matrix containing the features as columns and weights is a corresponding numpy array
        # create the predictions vector by using np.dot()
        predictions = np.dot(feature_matrix, weights)
        return(predictions)

    # see notes for this formula
    def feature_derivative(self, errors, feature):
        # Assume that errors and feature are both numpy arrays of the same length (number of data points)
        # compute twice the dot product of these vectors as 'derivative' and return the value
        derivative = 2 * np.dot(errors, feature)
        return(derivative)

    # compute Gradient Descent
    def regression_gradient_descent(self, feature_matrix, output, initial_weights, step_size, tolerance):
        converged = False
        weights = np.array(initial_weights) # make sure it's a numpy array       # vector
        # print "Initial Weights", weights
        while not converged:
            # compute the predictions based on feature_matrix and weights using your predict_output() function
            predictions = self.predict_output(feature_matrix, weights)            # vector
            # print "predictions", predictions, len(predictions)
            # compute the errors as predictions - output
            errors = predictions - output                                         # vector
            # print "errors", errors, len(errors)
            gradient_sum_squares = 0 # initialize the gradient sum of squares
            # while we haven't reached the tolerance yet, update each feature's weight
            for i in range(len(weights)): # loop over each weight
                # Recall that feature_matrix[:, i] is the feature column associated with weights[i]
                # compute the derivative for weight[i]:
                derivative = self.feature_derivative(errors, feature_matrix[:, i])  # scalar
                # print "derivative", derivative
                # add the squared value of the derivative to the gradient magnitude (for assessing convergence)
                gradient_sum_squares += (derivative * derivative)
                # subtract the step size times the derivative from the current weight
                weights[i] = weights[i] - (step_size * derivative)
            # compute the square-root of the gradient sum of squares to get the gradient matnigude:
            gradient_magnitude = sqrt(gradient_sum_squares)
            if gradient_magnitude < tolerance:
                converged = True
        # print "Final weights", weights
        return(weights)

    # Entry method
    def callme(self):
        print "++++++++++++++++++++++ Regression Week 2: Multiple Regression (gradient descent) ++++++++++++++++++++++"
        cmnHandle = Common()
        df_train = cmnHandle.readcsv("../data/kc_house_train_data.csv")
        df_test = cmnHandle.readcsv("../data/kc_house_test_data.csv")

        print '# *****************************************************************************************************'
        print '#                                           SIMPLE REGRESSION'
        print '# *****************************************************************************************************'
        simple_features = ['sqft_living']
        my_output = 'price'
        simple_feature_matrix = cmnHandle.AddConstantCol(cmnHandle.extract(df_train, simple_features)) # dataframe
        simple_feature_matrix = simple_feature_matrix.as_matrix()
        output = df_train[my_output]
        initial_weights = np.array([-47000., 1.])
        step_size = 7e-12
        tolerance = 2.5e7
        w_ = self.regression_gradient_descent(simple_feature_matrix, output, initial_weights, step_size, tolerance)
        # what is the value of the weight for sqft_living -- the second element of w_
        print w_
        # result printed = [-46999.88716555    281.91211918]

        # What is the predicted price for the 1st house in the TEST data set for model 1 (round to nearest dollar)?
        test_simple_feature_matrix = cmnHandle.AddConstantCol(cmnHandle.extract(df_test, simple_features)) # dataframe
        test_simple_feature_matrix = test_simple_feature_matrix.as_matrix()
        test_predictions = self.predict_output(test_simple_feature_matrix, w_)
        print "Predicted value of 1st house $%.0f" % test_predictions[0]
        # result printed = Predicted value of 1st house $356134

        # RSS [Simple Regression Model]
        print "RSS Simple Regression: %e" % np.sum(np.subtract(df_test[my_output], (w_[0] +
                                                (df_test[simple_features[0]] * w_[1])))**2)
        # result printed = RSS Simple Regression: 2.754000e+14

        print '# *****************************************************************************************************'
        print '#                                           MULTIPLE REGRESSION'
        print '# *****************************************************************************************************'
        model_features = ['sqft_living', 'sqft_living15'] # sqft_living15 is the average squarefeet for the nearest 15 neighbors.
        my_output = 'price'
        feature_matrix = cmnHandle.AddConstantCol(cmnHandle.extract(df_train, model_features))  # dataframe
        feature_matrix = feature_matrix.as_matrix()
        initial_weights = np.array([-100000., 1., 1.])
        output = df_train[my_output]
        step_size = 4e-12
        tolerance = 1e9
        wm_ = self.regression_gradient_descent(feature_matrix, output, initial_weights, step_size, tolerance)

        # What is the predicted price for the 1st house in the TEST data set for model 2 (round to nearest dollar)?
        feature_test_matrix = cmnHandle.AddConstantCol(cmnHandle.extract(df_test, model_features))  # dataframe
        test_predictions_m = self.predict_output(feature_test_matrix, wm_)
        print "Predicted value of 1st house $%.0f, actual price %.0f" % (test_predictions_m[0], df_test['price'][0])

        #RSS [Multiple Regression Model]
        print "RSS Multiple Regression: %e" % np.sum(np.subtract(df_test[my_output], (wm_[0] +
                                          (df_test[model_features[0]] * wm_[1]) +
                                          (df_test[model_features[0]] * wm_[2])))**2)
        print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"