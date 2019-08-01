# coding: UTF-8
import tensorflow as tf
m1 = tf.constant([[2, 2]])
m2 = tf.constant([[3],
                  [3]])
dot_operation = tf.matmul(m1, m2)
print(dot_operation)  # 这里并没有结果
# 使用seesion ，方法1
sess = tf.Session()
result = sess.run(dot_operation)
print(result)

