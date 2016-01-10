# These are my assignment project codes developed in python.
# Anyone can use these codes without any permission
#
# Contact info: Kishwar Kumar [kumar.kishwar@gmail.com]
# Country: France
#



__author__ = 'kishwarkumar'
__date__ = '10/1/16' '6:39 PM'

# imports
import pandas as pd
import numpy as np

class Common:

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

    def AddConstantCol(self, dataframe):
        df = pd.DataFrame({'constant': np.repeat(1, repeats=np.shape(dataframe)[0])})
        df_list = [df, dataframe]
        dfa = pd.concat(df_list, axis=1)
        dfa.colums = ['constant'] + list(dataframe.columns.values)
        return dfa
