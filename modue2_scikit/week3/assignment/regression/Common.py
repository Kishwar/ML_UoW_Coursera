# These are my assignment project codes developed in python.
# Anyone can use these codes without any permission
#
# Contact info: Kishwar Kumar [kumar.kishwar@gmail.com]
# Country: France
#

__author__ = 'kishwarkumar'
__date__ = '10/1/16' '8:34 PM'

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

    def polynomial_sframe(self, feature, degree):
        # assume that degree >= 1
        dfreturn = pd.DataFrame({'power_1': feature})
        # first check if degree > 1
        if degree > 1:
            # then loop over the remaining degrees:
            # range usually starts at 0 and stops at the endpoint-1. We want it to start at
            # 2 and stop at degree
            for power in range(2, degree+1):
                # first we'll give the column a name:
                name = 'power_' + str(power)
                # then assign poly_sframe[name] to the appropriate power of feature
                df = pd.DataFrame({name: feature**power})
                df_list = [dfreturn, df]
                dfreturn = pd.concat(df_list, axis=1)
        return dfreturn