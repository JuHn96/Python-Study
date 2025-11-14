import tensorflow as tf
import numpy as np
 
X = np.linspace(2, 10, num=50)
Y = np.random.rand(50)*10 + 2
Y.sort()
print('X = ', X)
print('Y = ', Y)

import matplotlib.pyplot as plt
plt.plot(X, Y, 'ro')
plt.show()

W = tf.Variable(np.zeros(()), name='weight')
b = tf.Variable(np.zeros(()), name='bias')


def linear_regression(x):
    return W*x + b
 
def mean_square(y_pred, y):
    return tf.reduce_mean(tf.square(y_pred - y))


epochs = 1000
optimizer = tf.optimizers.SGD()
 
for epoch in range(1, epochs + 1):
    with tf.GradientTape() as t:
        pred = linear_regression(X)
        loss = mean_square(pred, Y)
    
    # compute gradients
    gradients = t.gradient(loss, [W, b])
 
    # update W and b following gradients
    optimizer.apply_gradients(zip(gradients, [W, b]))
 
    if epoch % 50 == 0:
        print(f'{epoch} epoch : loss = {loss}, W = {W.numpy()}, b = {b.numpy()}')


plt.plot(X, Y, 'ro', label='Origin data')
plt.plot(X, np.array(W*X + b), label='Fitted line')
plt.legend()

plt.show()