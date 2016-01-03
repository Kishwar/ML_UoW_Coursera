#!/usr/bin/env python

import sys

# -------------------------------------------------------------------
# This reducer code will input a <word, value> input file and
# join words together.
# NOTE: Input will come as a group of lines with same word (i.e. key)
# -------------------------------------------------------------------

# Possible inputs to reducer
# 1. <word \t date count>
# 2. <word \t count>
#   |_____|  |__________|
#      |          |
#      |          |___ value = <date count> or <count>
#      |_____ Key = <word>

# Initialize variables
prev_word = " "
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
dates_to_output = []    # an empty list to hold dates for given word
day_cnt_to_output = []  # an empty list of day counts for a given word
line_cnt = 0
curr_word_total_cnt = 0

# Scan through lines
for line in sys.stdin:
    line = line.strip()
    key_value = line.split("\t")

    # print("line:" + line)         # TO DEBUG
    
    line_cnt += 1

    curr_word = key_value[0]   # key (see above graph) |   Key = <word>
    value_in = key_value[1]    # value (see above graph) | value = <date count> or <count>

    if curr_word != prev_word:
        if line_cnt > 1:
            for i in range(len(dates_to_output)):
                print('{0} {1} {2} {3}'.format(dates_to_output[i], prev_word,
                                               day_cnt_to_output[i], curr_word_total_cnt))
            # reset list
            dates_to_output = []
            day_cnt_to_output = []
        prev_word = curr_word

    # determine if it is <word, total-count> or <word, date day-count>
    if value_in[0:3] in months:  # if for example Apr-13 then take out Apr
        date_day = value_in.split()  # month and date
        dates_to_output.append(date_day[0])    # Month
        day_cnt_to_output.append(date_day[1])  # count
    else:
        curr_word_total_cnt = value_in         # count

for i in range(len(dates_to_output)):
    print('{0} {1} {2} {3}'.format(dates_to_output[i], prev_word,
                                   day_cnt_to_output[i], curr_word_total_cnt))
