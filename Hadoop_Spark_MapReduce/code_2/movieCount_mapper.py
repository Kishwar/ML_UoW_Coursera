#!/usr/bin/env python

import sys

# ---------------------------------------
# Creator: Kishwar KUMAR
# Course: Coursera UC San Diego
# Date: 02/01/2016
# Assignment: Week4.3
# --------------------------------------

# The above just indicates to use python to interpret this file

# -------------------------------------------------------------------------
# This mapper code will input a line of text and output <movie-name, count>
# or XXXX
# -------------------------------------------------------------------------


# loop to receive input from standard terminal / file
for line in sys.stdin:
    line = line.strip()               # strip for any carriage return
    key_value = line.split(",")       # split line into key, value   <word, count> / <date word, count>
    if key_value[1].isdigit():
        print("{0}\t{1}".format(key_value[0], key_value[1]))  # Hadoop default is tab separated key, value.
    else:
        if key_value[1][0:3] == 'ABC':
            print("{0}\t{1}".format(key_value[0], key_value[1]))  # Hadoop default is tab separated key,
