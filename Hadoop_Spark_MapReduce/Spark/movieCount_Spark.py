#!/usr/bin/env python

# ----------------------------------------
# Creator: Kishwar KUMAR
# Course: Coursera UC San Diego
# Date: 04/01/2016
# Assignment: Week5.2
# ---------------------------------------


def split_show_views(line):
    line = line.split(",")
    return line[0], line[1]


def split_show_channel(line):
    line = line.split(",")
    return line[0], line[1]


def sum_function(a, b):
    return int(a) + int(b)


def extract_channel_views(show_view_channel):
    return show_view_channel[1][0], show_view_channel[1][1]  # <--(u'PostModern_Cooking', (u'DEF', u'1038'))

# step0: launch spark.. PYSPARK_DRIVER_PYTHON=ipython pyspark

# step1: read into Spark all of them with a pattern matching
         # show_views_file = sc.textFile("/user/cloudera/input7/join2_gennum?.txt")
# step2: use 'take' action > show_views_file.take(2)
         # expected outcome = Out[3]: [u'Hourly_Sports,21', u'PostModern_Show,38']
# step3: develop split_show_views(line)
# step4: # call show_views = show_views_file.map(split_show_views)

# step5: read into Spark all of them with a pattern matching
         # show_channel_file = sc.textFile("/user/cloudera/input7/join2_genchan?.txt")
# step6: develop split_show_channel(line)
# step7: call show_channel = show_channel_file.map(split_show_channel)

# step8: join 2 RDDs joined_dataset = show_channel.join(show_views)
         # expected output
                    # Out[12]:
                         # [(u'PostModern_Cooking', (u'DEF', u'1038')),
                         # (u'PostModern_Cooking', (u'DEF', u'415'))]
# step9: Extract channel as key
         # develop extract_channel_views(show_view_channel)
# step10: call channel_views = joined_dataset.map(extract_channel_views)
# step11: develop some across all channels function (sum_function(a,b))
# step12: call channel_views.reduceByKey(sum_function).collect() <-- get data to driver
