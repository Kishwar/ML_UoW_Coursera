#!/usr/bin/env python
# ---------------------------------------
# Creator: Kishwar KUMAR
# Course: Coursera UC San Diego
# Date: 01/-1/2016
# Assignment: Week4.1
# --------------------------------------

# The above just indicates to use python to interpret this file

# ---------------------------------------------------------------------
# This mapper code will input a line of text and output <word, 1>
# ---------------------------------------------------------------------

import sys  # python module with system functions for this OS

# loop to receive input from standard terminal / file
for line in sys.stdin:
    line = line.strip()
    keys = line.split()
    for key in keys:
        value = 1
        print("{0}\t{1}".format(key, value))  # Hadoop default is tab separated key, value.
