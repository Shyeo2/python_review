'''


'''

import os
import numpy as np
import tensorflow as tf

# 로그레벨이 3이 되면 warning이 뜨지 않음
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

x = tf.Variable([3.0, 4.0])
y = tf.Variable([1.0, 2.0])

with tf.GradientTape() as tape:
    z = x + y
    loss = tf.math.reduce_mean(z)

dx = tape.gradient(loss, x)
print(dx)

'''
    TensorFlow에서는 변수가 아닌 상수라면 기본적으로 기울기는 측정하지 않음 (not watched)
'''
x = tf.linspace(-10, 10, 100)

with tf.GradientTape() as tape:
    tape.watch(x)           # constant이므로 watch()함수 호출 필요
    y = tf.nn.sigmoid(x)

dx = tape.gradient(y, x)
print(dx)

import matplotlib.pyplot as plt

plt.plot(x, y, 'r', label="y")
plt.plot(x, dx, 'b--', label="dx/dy")
plt.legend()
plt.show()
