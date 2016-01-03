#!/usr/bin/env python

import sys

# -------------------------------------------------------------------
# This mapper code will input a <date word, value> input file and
# move date into value field for output.
# -------------------------------------------------------------------

# Possible inputs to mapper
# 1. <date word, count>
# 2. <word,      count>
#   |__________||_____|
#      |          |
#      |          |___ <count>
#      |_____ Key <date word > or <word>

# Outputs (by mapper)
# 1. <word \t date count>
# 2. <word \t count>
#   |_____||____________|
#      |         |
#      |         |__ value = <date count> or <count>
#      |____ key = <word>

# Read through lines
for line in sys.stdin:
    line = line.strip()               # strip for any carriage return
    key_value = line.split(",")       # split line into key, value   <word, count> / <date word, count>
    key_in = key_value[0].split(" ")  # Key is first item in the list <word> / <date word>
    value_in = key_value[1]           # value is 2nd item in the list <count>

    # Print key_in
    if len(key_in) >= 2:    # If this entry has <date word> in key
        date = key_in[0]   # date = key
        word = key_in[1]   # word = value
        value_out = date + " " + value_in                 # <date count>
        print('%s\t%s' % (word, value_out))               # <word \t date count>
    else:
        print('%s\t%s' % (key_in[0], value_in))           # <word \t count>

# Note that Hadoop expects a tab to separate key value
# but this program assumes the input file as a "," separating key value
