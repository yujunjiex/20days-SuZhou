# coding: UTF-8
import tensorflow as tf

x1 = tf.placeholder(dtype="float", shape=[2, 1])
x2 = tf.placeholder(dtype="float", shape=[1, 2])
z = tf.matmul(x1, x2)


with tf.Session() as sess:
    res = sess.run(z, feed_dict={x1: [[2], [2]], x2: [[3, 3]]})
    print(res)
