# These are my assignment project codes developed in python.
# Anyone can use these codes without any permission
#
# Contact info: Kishwar Kumar [kumar.kishwar@gmail.com]
# Country: France
#

# imports
import pandas as pd
import numpy as np

__author__ = 'kishwarkumar'
__date__ = '6/1/16' '9:15 PM'

# Function reads CSV and retuns dataframe
def ReadCSV(path):
    return pd.read_csv(path)

def simple_linear_regression(input_feature, output):
    # compute the mean of  input_feature and output
    # compute the product of the output and the input_feature and its mean
    # compute the squared value of the input_feature and its mean
    # use the formula for the slope
    # use the formula for the intercept

    feature_sum = input_feature.sum()
    output_sum = output.sum()
    feature_output_vector_sum = (output * input_feature).sum()
    input_feature_sq_sum = (input_feature * input_feature).sum()
    N_Size = len(input_feature)
    W1_slope = (feature_output_vector_sum - ((output_sum * feature_sum)/N_Size)) / \
               (input_feature_sq_sum - ((feature_sum * feature_sum)/N_Size))
    Wo_Intercept = (output_sum / N_Size) - (W1_slope * (feature_sum / N_Size))
    intercept = Wo_Intercept
    slope = W1_slope
    return (intercept, slope)

def get_regression_predictions(input_feature, intercept, slope):
    # calculate the predicted values:
    # input_feature is scalar quantity.. intercept and slope are also scalar
    predicted_values = intercept + (slope * input_feature)
    return predicted_values

def get_residual_sum_of_squares(input_feature, output, intercept, slope):
    # First get the predictions
    # then compute the residuals (since we are squaring it doesn't matter which order you subtract)
    # square the residuals and add them up
    #input_feature and output are vectors
    #intercept and slope are scalar
    err = output - (intercept + (slope * input_feature))
    err_sq = err * err
    RSS = err_sq.sum()
    return(RSS)

def inverse_regression_predictions(output, intercept, slope):
    # solve output = slope + intercept*input_feature for input_feature. Use this equation to compute the inverse predictions:
    # y = wo + w1x
    # y - w0 = w1x
    # x = (y - w0) / w1
    estimated_feature = (output - intercept) / slope
    return estimated_feature

if __name__ == "__main__":
    DFTrain = ReadCSV("../data/kc_house_train_data.csv")
    DFTest = ReadCSV("../data/kc_house_test_data.csv")

    # Lets see what is average of price in Training set
    prices = DFTrain['price']
    Avg = sum(prices) / len(prices)
    print("Price Average = %.f, using mean = %.f" % (Avg, np.mean(Avg)))

    # Test Simple Linear regression method
    test_feature = np.array(range(5))
    test_output = np.array(1 + 1*test_feature)
    (test_intercept, test_slope) =  simple_linear_regression(test_feature, test_output)
    print "Intercept: " + str(test_intercept)    # should be 1
    print "Slope: " + str(test_slope)            # should be 1

    # Simple Linear model
    sqft_intercept, sqft_slope = simple_linear_regression(DFTrain['sqft_living'], \
                                                      DFTrain['price'])

    print "Intercept: " + str(sqft_intercept)
    print "Slope: " + str(sqft_slope)

    # We have got Intercept and Slope.. Lets predict
    my_house_sqft = 2650
    estimated_price = get_regression_predictions(my_house_sqft, sqft_intercept, sqft_slope)
    print "The estimated price for a house with %d squarefeet is $%.2f" % \
                                                    (my_house_sqft, estimated_price)

    # Lets calculate RSS (Residual Sum Of Square) of our model
    print get_residual_sum_of_squares(test_feature, test_output, test_intercept, test_slope) # should be 0.0
    rss_prices_on_sqft = get_residual_sum_of_squares(DFTrain['sqft_living'], \
                                                 DFTrain['price'], \
                                                 sqft_intercept, sqft_slope)
    print 'The RSS of predicting Prices based on Square Feet is : ' + str(rss_prices_on_sqft)

    # Predict the squarefeet given price
    my_house_price = 800000
    estimated_squarefeet = inverse_regression_predictions(my_house_price, \
                                                      sqft_intercept, \
                                                      sqft_slope)
    print "The estimated squarefeet for a house worth $%.2f is %d" % \
                                            (my_house_price, estimated_squarefeet)

    # Estimate the slope and intercept for predicting 'price' based on 'bedrooms'
    bedroom_intercept, bedroom_slope = simple_linear_regression(DFTrain['bedrooms'], \
                                                      DFTrain['price'])

    print "Intercept: " + str(bedroom_intercept)
    print "Slope: " + str(bedroom_slope)

    # Compute RSS when using bedrooms on TEST data:
    err_bedrooms = DFTest['price'] - (bedroom_intercept + \
                                     (DFTest['bedrooms'] * bedroom_slope))
    err_bedrooms_sq = err_bedrooms * err_bedrooms
    RSS_bedrooms_model = err_bedrooms_sq.sum()
    print "RSS Bedrooms Model: " + str(RSS_bedrooms_model)

    # Compute RSS when using squarfeet on TEST data:
    err_sqft = DFTest['price'] - (sqft_intercept + \
                                     (DFTest['bedrooms'] * sqft_slope))
    err_sqft_sq = err_sqft * err_sqft
    RSS_sqft_model = err_sqft_sq.sum()
    print "RSS sqft Model: " + str(RSS_sqft_model)