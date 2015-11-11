# These codes are developed using book "Mastering Python for Data Science.pdf"
# Developed by: Kishwar KUMAR
# Date: 11/nov/2015
# Email: kumar.kishwar@gmail.com
# Software Used: PyCharm (Community License)
# Operating System: OSX


__author__ = 'kishwarkumar'

import os

class ChangeDir:

    # Define constructor
    def __init__(self):
        return

    def SetDir(self, Path):
        self.Path = Path

    # Change Path Method
    def ChangeIt(self):
        os.chdir(self.Path)

    # Path getter
    def GetPath(self):
        return self.Path
