import tensorflow as tf
import os
import numpy as np
count = 0
M=0
F=0
for example in tf.python_io.tf_record_iterator("/home/team/datasets/tarball/tfrecords/up140_mtc_test.tfrecords"):

    result = tf.train.Example.FromString(example)
    # print(result.features.feature['gender'].int64_list.value)
    # print(result.features.feature['age'].int64_list.value)
    count = count + 1
    # if i in a:
    #     print(result.features.feature['gender'].int64_list.value)
    #     print(result.features.feature['age'].int64_list.value)
    

    # print(result.features.feature['age'].int64_list.value)     
    if result.features.feature['gender'].int64_list.value[0] == 0:
        M=M+1
    else:
        F=F+1
    print(result.features.feature['gender'].int64_list.value)
print(count)
print('M = ', M)
print('F = ', F)