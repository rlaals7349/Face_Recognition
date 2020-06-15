import tensorflow as tf
import os


i = 0
for example in tf.python_io.tf_record_iterator("/home/team/datasets/tfrecords/test.tfrecords"):
    
    result = tf.train.Example.FromString(example)

    i = i + 1
    if i == 500 :
        print(result.features.feature['gender'].int64_list.value)
        print(result.features.feature['age'].int64_list.value)
    if i == 500 :
        break 


