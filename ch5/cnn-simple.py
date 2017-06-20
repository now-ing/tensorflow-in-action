#-*-coding:utf8-*-

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

data_path="/usr/bigdata/data/mnist_data/"

mnist=input_data.read_data_sets(data_path, one_hot=True)

sess=tf.InteractiveSession()

def weight_variable(shape):
    initial=tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial=tf.constant(0.1, shape=shape)
    return tf.Variable(initial)
