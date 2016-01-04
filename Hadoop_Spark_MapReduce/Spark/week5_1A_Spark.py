#!/usr/bin/env python

# ----------------------------------------
# Creator: Kishwar KUMAR
# Course: Coursera UC San Diego
# Date: 03/01/2016
# Assignment: Week5.1
# ---------------------------------------


def split_file_a(line):
    # split the input line in word and count on the comma
    line = line.split(",")
    # return key and value
    return line[0], int(line[1])


def split_file_b(line):
    # split the input line into word, date and count_string
    line1 = line.split(",")        # <Jan-01 able,5>
    line2 = line1[0].split()
    return line2[1], line2[0] + ' ' + line1[1]


# step0: launch spark.. PYSPARK_DRIVER_PYTHON=ipython pyspark
# step1: copy join1_FilaA.txt to /user/cloudera/input6 using hdfs dfs -put
# step2: copy join1_fileB.txt to /user/cloudera/input6 using hdfs dfs -put
# step3: fileA = sc.textFile("/user/cloudera/input6/join1_FileA.txt")
# step4: fileB = sc.textFile("/user/cloudera/input6/join1_fileB.txt")
# step6: check data using fileA.collect() or fileB.collect()

# step7: call above function
# step8: fileA_data = fileA.map(split_file_a)  # call map over FileA
# step9: fileA_data.collect()  # to see output

# step10: call above function
# step11: fileB_data = fileB.map(split_file_b)  # call map over fileB
# step12: fileB_data.collect()  # to see output

# step13: join operation
# step14: fileB_joined_fileA = fileB_data.join(fileA_data)
# step15: fileB_joined_fileA.collect() # to see output
