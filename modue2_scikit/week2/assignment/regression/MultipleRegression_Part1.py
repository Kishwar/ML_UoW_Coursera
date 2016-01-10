# These are my assignment project codes developed in python.
# Anyone can use these codes without any permission
# Regression Week 2: Multiple Regression (Interpretation)
#
# Contact info: Kishwar Kumar [kumar.kishwar@gmail.com]
# Country: France
#

__author__ = 'kishwarkumar'
__date__ = '6/1/16' '10:07 PM'

# imports
from sklearn import linear_model
import numpy as np
from common import Common

class MultipleRegressionPart1:

    # Define constructor
    def __init__(self):
        return

    # training
    def multiregression(self, lm_handle, training_matrix, output_vector):
        model_ = lm_handle.fit(training_matrix, output_vector)
        w_ = [model_.intercept_]
        dim = np.shape(training_matrix)
        for j in range(dim[1]):
            w_.append(model_.coef_[j])
        return w_, model_

    # Entry method
    def callme(self):
        print "++++++++++++++++++++++ Regression Week 2: Multiple Regression (Interpretation) ++++++++++++++++++++++"
        cmnHandle = Common()
        df_train = cmnHandle.readcsv("../data/kc_house_train_data.csv")
        df_test = cmnHandle.readcsv("../data/kc_house_test_data.csv")
        example_features = ['sqft_living', 'bedrooms', 'bathrooms']
        df_updated = cmnHandle.extract(df_train, example_features)

        # create Linear Regression model handle
        lm = linear_model.LinearRegression()

        # Train model and calculate weights
        w_, model_ = self.multiregression(lm, df_updated, df_train['price'])

        # Lets predict
        df_test_updated = cmnHandle.extract(df_test, example_features)
        predict_ex = model_.predict(df_test_updated)
        print "Predicted Price %.2f, Original Price %.2f" % (predict_ex[0], df_test['price'][0])
        # result printed = Predicted Price 350640.94, Original Price 310000.00

        # Lets calculate RSS
        rss_ = cmnHandle.get_residual_sum_of_squares(model_, df_test_updated, df_test['price'])
        print "RSS %e" % rss_
        # result printed = RSS 2.737619e+14

        # Lets increase model complexity
        # Model 1: squarefeet, # bedrooms, # bathrooms, latitude & longitude
        # Model 2: add bedrooms*bathrooms
        # Model 3: Add log squarefeet, bedrooms squared, and the (nonsensical) latitude + longitude
        model_1_features = ['sqft_living', 'bedrooms', 'bathrooms', 'lat', 'long']
        model_2_features = model_1_features + ['bed_bath_rooms']
        model_3_features = model_2_features + ['bedrooms_squared', 'log_sqft_living', 'lat_plus_long']

        df_train, df_test = cmnHandle.create_and_update_df(df_train, df_test)

        train_set_model_1 = cmnHandle.extract(df_train, model_1_features)
        train_set_model_2 = cmnHandle.extract(df_train, model_2_features)
        train_set_model_3 = cmnHandle.extract(df_train, model_3_features)
        test_set_model_1 = cmnHandle.extract(df_test, model_1_features)
        test_set_model_2 = cmnHandle.extract(df_test, model_2_features)
        test_set_model_3 = cmnHandle.extract(df_test, model_3_features)

        # create Linear Regression model handle
        lm_1 = linear_model.LinearRegression()
        lm_2 = linear_model.LinearRegression()
        lm_3 = linear_model.LinearRegression()

        # lets train system using above features
        w_1, model_a = self.multiregression(lm_1, train_set_model_1, df_train['price'])
        w_2, model_b = self.multiregression(lm_2, train_set_model_2, df_train['price'])
        w_3, model_c = self.multiregression(lm_3, train_set_model_3, df_train['price'])

        # compare models using RSS on training data
        rss_1 = cmnHandle.get_residual_sum_of_squares(model_a, train_set_model_1, df_train['price'])
        rss_2 = cmnHandle.get_residual_sum_of_squares(model_b, train_set_model_2, df_train['price'])
        rss_3 = cmnHandle.get_residual_sum_of_squares(model_c, train_set_model_3, df_train['price'])
        print("rss_1 %e, rss_2 %e, rss_3 %e" % (rss_1, rss_2, rss_3))
        # result printed = rss_1 9.678800e+14, rss_2 9.584196e+14, rss_3 9.034365e+14

        # compare models using RSS on test data
        rss_1 = cmnHandle.get_residual_sum_of_squares(model_a, test_set_model_1, df_test['price'])
        rss_2 = cmnHandle.get_residual_sum_of_squares(model_b, test_set_model_2, df_test['price'])
        rss_3 = cmnHandle.get_residual_sum_of_squares(model_c, test_set_model_3, df_test['price'])
        print("rss_1 %e, rss_2 %e, rss_3 %e" % (rss_1, rss_2, rss_3))
        # result printed = rss_1 2.255005e+14, rss_2 2.233775e+14, rss_3 2.592363e+14

        print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"