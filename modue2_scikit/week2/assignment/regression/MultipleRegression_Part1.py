# These are my assignment project codes developed in python.
# Anyone can use these codes without any permission
#
# Contact info: Kishwar Kumar [kumar.kishwar@gmail.com]
# Country: France
#

__author__ = 'kishwarkumar'
__date__ = '6/1/16' '10:07 PM'

# imports
import pandas as pd
from sklearn import linear_model
import numpy as np


class MultipleRegressionPart1:

    # Define constructor
    def __init__(self):
        return

    # Function reads CSV and retuns dataframe
    def readcsv(self, path):
        return pd.read_csv(path)

    # Extract feature from DataFrame and generate new DataFrame
    def extract(self, df_input, features):
        df1 = pd.DataFrame(df_input[features[0]])
        lp_index = 0
        for feature in features:
            if lp_index == 0:
                lp_index += 1
                continue
            df2 = pd.DataFrame(df_input[feature])
            dfa_list = [df1, df2]
            df1 = pd.concat(dfa_list, axis=1)
        return df1

    # training
    def multiregression(self, lm_handle, training_matrix, output_vector):
        model_ = lm_handle.fit(training_matrix, output_vector)
        w_ = [model_.intercept_]
        dim = np.shape(training_matrix)
        for j in range(dim[1]):
            w_.append(model_.coef_[j])
        return w_, model_

    # calculate RSS
    def get_residual_sum_of_squares(self, model, data, outcome):
        rss = 0
        # First get the predictions
        predictions = model.predict(data)
        # Then compute the residuals/errors
        rss_err = outcome - predictions
        # Then square and add them up
        rsserrsq = rss_err * rss_err
        rss_ = rsserrsq.sum()
        return(rss_)

    # artificial features
    def create_and_update_df(self, df_train, df_test):
        # bedrooms_squared / bed_bath_rooms / log_sqft_living
        df0 = pd.DataFrame(df_train['bedrooms'])
        df1 = pd.DataFrame(df_train['bedrooms']**2)
        df2 = pd.DataFrame(df_train['bedrooms'] * df_train['bathrooms'])
        df3 = pd.DataFrame(np.log(df_train['sqft_living']))
        df4 = pd.DataFrame(df_train['lat'] + df_train['long'])
        df_list = [df_train, df1, df2, df3, df4]
        dfa = pd.concat(df_list, axis=1)
        dfa.columns = list(df_train.columns.values) + ['bedrooms_squared', 'bed_bath_rooms', 'log_sqft_living', 'lat_plus_long']

        # bedrooms_squared / bed_bath_rooms / log_sqft_living
        df0 = pd.DataFrame(df_test['bedrooms'])
        df1 = pd.DataFrame(df_test['bedrooms']**2)
        df2 = pd.DataFrame(df_test['bedrooms'] * df_test['bathrooms'])
        df3 = pd.DataFrame(np.log(df_test['sqft_living']))
        df4 = pd.DataFrame(df_test['lat'] + df_test['long'])
        df_list = [df_test, df1, df2, df3, df4]
        dfb = pd.concat(df_list, axis=1)
        dfb.columns = list(df_test.columns.values) + ['bedrooms_squared', 'bed_bath_rooms', 'log_sqft_living', 'lat_plus_long']

        return dfa, dfb

    # Entry method
    def callme(self):
        df_train = self.readcsv("../data/kc_house_train_data.csv")
        df_test = self.readcsv("../data/kc_house_test_data.csv")
        example_features = ['sqft_living', 'bedrooms', 'bathrooms']
        df_updated = self.extract(df_train, example_features)

        # create Linear Regression model handle
        lm = linear_model.LinearRegression()

        # Train model and calculate weights
        w_, model_ = self.multiregression(lm, df_updated, df_train['price'])

        # Lets predict
        df_test_updated = self.extract(df_test, example_features)
        predict_ex = model_.predict(df_test_updated)
        print "Predicted Price %.2f, Original Price %.2f" % (predict_ex[0], df_test['price'][0])
        # result printed = Predicted Price 350640.94, Original Price 310000.00

        # Lets calculate RSS
        rss_ = self.get_residual_sum_of_squares(model_, df_test_updated, df_test['price'])
        print "RSS %e" % rss_
        # result printed = RSS 2.737619e+14

        # Lets increase model complexity
        # Model 1: squarefeet, # bedrooms, # bathrooms, latitude & longitude
        # Model 2: add bedrooms*bathrooms
        # Model 3: Add log squarefeet, bedrooms squared, and the (nonsensical) latitude + longitude
        model_1_features = ['sqft_living', 'bedrooms', 'bathrooms', 'lat', 'long']
        model_2_features = model_1_features + ['bed_bath_rooms']
        model_3_features = model_2_features + ['bedrooms_squared', 'log_sqft_living', 'lat_plus_long']

        df_train, df_test = self.create_and_update_df(df_train, df_test)

        train_set_model_1 = self.extract(df_train, model_1_features)
        train_set_model_2 = self.extract(df_train, model_2_features)
        train_set_model_3 = self.extract(df_train, model_3_features)
        test_set_model_1 = self.extract(df_test, model_1_features)
        test_set_model_2 = self.extract(df_test, model_2_features)
        test_set_model_3 = self.extract(df_test, model_3_features)

        # create Linear Regression model handle
        lm_1 = linear_model.LinearRegression()
        lm_2 = linear_model.LinearRegression()
        lm_3 = linear_model.LinearRegression()

        # lets train system using above features
        w_1, model_a = self.multiregression(lm_1, train_set_model_1, df_train['price'])
        w_2, model_b = self.multiregression(lm_2, train_set_model_2, df_train['price'])
        w_3, model_c = self.multiregression(lm_3, train_set_model_3, df_train['price'])

        # compare models using RSS on training data
        rss_1 = self.get_residual_sum_of_squares(model_a, train_set_model_1, df_train['price'])
        rss_2 = self.get_residual_sum_of_squares(model_b, train_set_model_2, df_train['price'])
        rss_3 = self.get_residual_sum_of_squares(model_c, train_set_model_3, df_train['price'])
        print("rss_1 %e, rss_2 %e, rss_3 %e" % (rss_1, rss_2, rss_3))
        # result printed = rss_1 9.678800e+14, rss_2 9.584196e+14, rss_3 9.034365e+14

        # compare models using RSS on test data
        rss_1 = self.get_residual_sum_of_squares(model_a, test_set_model_1, df_test['price'])
        rss_2 = self.get_residual_sum_of_squares(model_b, test_set_model_2, df_test['price'])
        rss_3 = self.get_residual_sum_of_squares(model_c, test_set_model_3, df_test['price'])
        print("rss_1 %e, rss_2 %e, rss_3 %e" % (rss_1, rss_2, rss_3))
        # result printed = rss_1 2.255005e+14, rss_2 2.233775e+14, rss_3 2.592363e+14

