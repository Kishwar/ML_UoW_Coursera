#!/usr/bin/env python

# ----------------------------------------
# Creator: Kishwar KUMAR
# Course: Coursera UC San Diego
# Date: 02/01/2016
# Assignment: Week4.1
# ---------------------------------------

# The above just indicates to use python to interpret this file

# --------------------------------------------------------------------------
# This reducer code will input a line of text and output <movie-name, count>
# or XXXXX
# --------------------------------------------------------------------------

import sys

initCounter = 0
LoopNum = 0
PrevMovie = ' '
ABCFound = False

# loop to receive input from standard terminal / file
for line in sys.stdin:
    line = line.strip()

    key_value = line.split("\t")

    # Debug
    # if(key_value[0] == "Almost_News"):
    #    print("line: " + line)

    # Here Key_value has following possibilities
    #   1. <movie name, count>   <--- this can be from any channel
    #   2. <movie name, 'ABC'>

    LoopNum += 1
    CurrMovie = key_value[0]   # <-- movie name
    CurrValue = key_value[1]   # <-- count or ABC

    if CurrMovie != PrevMovie:
        if LoopNum > 1:
            if ABCFound:
                ABCFound = False
                print("{0} {1}".format(PrevMovie, initCounter))
                if CurrValue != 'ABC':
                    initCounter = int(CurrValue)
                else:
                    initCounter = 0
            else:
                initCounter = int(CurrValue)
        else:
            initCounter = int(CurrValue)
        PrevMovie = CurrMovie
    else:
        if CurrValue != 'ABC':
            initCounter += int(CurrValue)
            PrevMovie = CurrMovie
        else:
            ABCFound = True
            PrevMovie = CurrMovie
