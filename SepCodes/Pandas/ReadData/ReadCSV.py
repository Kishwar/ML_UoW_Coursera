# These codes are developed using book "Mastering Python for Data Science.pdf"
# Developed by: Kishwar KUMAR
# Email: kumar.kishwar@gmail.com
# Software Used: PyCharm (Community License)
# Operating System: OSX

import pandas as pd

class Read_CSV:

    # Define constructor
    def __init__(self):
        return

    def Read(self, Path):
        self.path = Path    #save path
        return pd.read_csv(Path)

    def GetPath(self):
        return self.path