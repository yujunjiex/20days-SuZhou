# coding: UTF-8
import tensorflow as tf

m1 = tf.constant([[2, 2]])      # 一个常量初始化操作
m2 = tf.constant([[3], [3]])

print(m1)
print(m2)


sess = tf.Session()
print(sess.run(m1))
print(sess.run(m2))


with tf.Session() as sess:
    m3 = tf.matmul(m1, m2)
    print(sess.run(m3))
