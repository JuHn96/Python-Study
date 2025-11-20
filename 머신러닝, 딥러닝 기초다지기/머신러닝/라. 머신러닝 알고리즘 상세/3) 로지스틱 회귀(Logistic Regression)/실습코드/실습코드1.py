from sklearn.datasets import load_iris
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iris_data = sklearn.datasets.load_iris()
 
dataset = pd.DataFrame(data=np.c_[iris_data['data'], iris_data['target']], columns=iris_data['feature_names']+['target']).astype('float32')
print(dataset.head())
print(iris_data['target_names'])
print(dataset.describe())

dataset = dataset.sample(frac=1).reset_index(drop=True)
print(dataset.head())

m_train = 100
m_test = 50
num_features = 4
num_classes = 3
 
x_train = dataset.iloc[:m_train, :num_features]
y_train = dataset.iloc[:m_train, num_features]
x_test = dataset.iloc[m_train:, :num_features]
y_test = dataset.iloc[m_train:, num_features]
 
print(f'x_train shape : {x_train.shape}') # (100, 4)
print(f'y_train shape : {y_train.shape}') # (100, )
print(f'x_test shape : {x_test.shape}')   # (50, 4)
print(f'y_test shape : {y_test.shape}')   # (50, )

# 평균 and 표준편차 계산
mean = x_train.mean()
std = x_train.std()

# normalization
x_train = (x_train - mean) / std
x_test = (x_test - mean) / std
 
print(x_train.describe())


#학습
def logistic_regression(X, W, b):
    return tf.math.sigmoid(tf.matmul(X, W) + b)
 
def compute_cost(y_hat, y):
    y_orig = tf.one_hot(y, num_classes)
    cost = -tf.reduce_mean(tf.reduce_sum(y_orig*tf.math.log(y_hat) + (1-y_orig)*tf.math.log(1-y_hat), 1))
 
    return cost
 
def predict(y_hat):
    return tf.argmax(y_hat, 1)
 
def accuracy(y_pred, y):
    correct_pred = tf.equal(y_pred, tf.cast(y, tf.int64))
    return tf.reduce_mean(tf.cast(correct_pred, tf.float32))


def model(X_train, Y_train, X_test, Y_test, num_iteration=2000, learning_rate=0.01, opt='SGD'):
    # parameter initialization
    W = tf.Variable(tf.zeros([num_features, num_classes]), name='weight')
    b = tf.Variable(tf.zeros([num_classes]), name='bias')
    
    # select optimization algorithm
    if opt == 'SGD':
        optimizer = tf.optimizers.SGD(learning_rate=learning_rate)
    elif opt == 'Adam':
        optimizer = tf.optimizers.Adam(learning_rate=learning_rate)
    
    costs = []
    accs = []
 
    for iter in range(1, num_iteration + 1):
        with tf.GradientTape() as tape:
            y_hat = logistic_regression(X_train,W, b)
            cost = compute_cost(y_hat, Y_train)
        
        # compute gradient
        grads = tape.gradient(cost, [W, b])
 
        # update gradient
        optimizer.apply_gradients(zip(grads, [W, b]))
 
        # predict 
        pred = predict(y_hat)
        # compute accuracy
        acc = accuracy(pred, Y_train)
 
        # save status
        costs.append(cost)
        accs.append(acc)
 
        # print status
        if iter % 100 == 0:
            print(f'{iter} iterations : cost = {cost}, acc = {acc*100} %')
    
    # predict on test data
    y_pred = predict(logistic_regression(X_test, W, b))
    test_acc = accuracy(y_pred, Y_test)
 
    print(f'acc on test data : {test_acc*100} %')
 
    ret = {
        'weight':W,
        'bias':b,
        'costs':costs,
        'accs':accs
    }
 
    return ret

# SGD, iteration = 5000, learning_rate = 0.01
# opt1 = model(x_train, y_train, x_test, y_test, num_iteration=5000, learning_rate=0.01, opt='SGD')

# Adam, iteration = 5000, learning_rate = 0.01
opt2 = model(x_train, y_train, x_test, y_test, num_iteration=5000, learning_rate=0.01, opt='Adam')
