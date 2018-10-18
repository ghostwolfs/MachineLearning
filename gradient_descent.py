import numpy as np

train_x = np.array(([1,1],[2,1]))
train_y = np.array(([1],[3]))
rate = 0.01

def cost_function(x, y, theta):
    '''caculate the cost of this model'''
    cost_vecter = np.dot(x, theta) - y
    return np.dot(np.transpose(cost_vecter), cost_vecter)*(1/2)

def gradient_function(x, y, theta):
    '''caculate the gradient of this theta'''
    diffrence = np.dot(x, theta) - y
    return (1/2)*np.dot(np.transpose(x), diffrence)

def gradient_descent(x, y, theta):
    '''the main function of gradient descent'''
    theta = np.array(([1],[1]))
    gradient = gradient_function(x, y, theta)
    while np.all(np.absolute(gradient) >= 1e-5):
        theta = theta - rate*gradient
        gradient = gradient_function(x, y, theta)
    return theta

print(gradient_descent(train_x, train_y, rate))

# print(cost_function(train_x,train_y,np.array(([1],[1]))))
