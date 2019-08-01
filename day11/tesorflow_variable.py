# coding: UTF-8
import tensorflow as tf

var = tf.Variable(0)    # 相当于变量初始化操作

add_operation = tf.add(var, 1)  # 这是一个加1操作
update_operation = tf.assign(var, add_operation)    # 这是一个赋值操作


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())   # 初始化所有的全局变量(变量必须用这种方式)

    sess.run(update_operation)
    sess.run(update_operation)
    print(sess.run(var))
