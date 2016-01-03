#!/usr/bin/env python
# ----------------------------------------
# Creator: Kishwar KUMAR
# Course: Coursera UC San Diego
# Date: 01/-1/2016
# Assignment: Week4.1
# ---------------------------------------

# The above just indicates to use python to interpret this file

# --------------------------------------------------------------------------
# This reducer code will input a line of text and output <word, total-count>
# --------------------------------------------------------------------------

import sys  # python module with system functions for this OS

last_key = None
running_total = 0

# loop through file
for input_line in sys.stdin:
    input_line = input_line.strip()
    this_key, value = input_line.split("\t", 1)  # Hadoop default was tab separated values
    value = int(value)
    # Key check part
    if last_key == this_key:
        running_total += value
    else:
        if last_key:
            print("{0}\t{1}".format(last_key, running_total))
        running_total = value
        last_key = this_key

if last_key == this_key:
    print("{0}\t{1}".format(last_key, running_total))
