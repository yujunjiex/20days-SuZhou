# coding: UTF-8
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
# 创建期望值x_data和y_data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

### 创建神经网络结构，包含Weights和biases，是我们需要预测的两个值 ###
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))
# 通过Weights和biases计算y值
y = Weights * x_data + biases
# 计算loss
loss = tf.reduce_mean(tf.square(y - y_data))
# 梯度下降优化器
optimizer = tf.train.GradientDescentOptimizer(0.5)
# 最小化loss
train = optimizer.minimize(loss)
# 开启session，并初始化全局变量
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
# 训练
for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))
        y_result = sess.run(y)
        # 清空窗口
        plt.cla()
        # 期望值图形表示
        plt.scatter(x_data, y_data)
        # 实际值图像表示
        plt.plot(x_data, y_result, 'r-', lw=5)

        plt.pause(0.3)

plt.ioff()
plt.show()
