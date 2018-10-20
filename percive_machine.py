import numpy as np

theta = np.array([0.00,1.00,0.00]).reshape(3,1)
train_x = np.array(([1,2],[2,1]))
constant_c = np.ones((2,1))
train_x = np.hstack((train_x,constant_c))
train_y = np.array(([1],[0]))
rate = 0.05
# print(train_x)

def percive_machine(x, y, theta, rate):
	neurons_output = np.dot(train_x, theta)
	for index in range(len(neurons_output)):
		if neurons_output[index] >= 0:
			neurons_output[index] = 1
		else:
			neurons_output[index] = 0
	difference = train_y - neurons_output
	# print(difference)
	if np.all(difference == 0):
		print(theta)
	else:
		for index in range(len(difference)):
			if difference[index] != 0:
				# index = 1
				# print(difference[index])
				change_w = rate*np.dot(train_x[index:index+1,0:2], difference)
				change_b = rate*difference[index]
				print(change_w, change_b, theta[index])
				print(theta[index] + change_w)
				theta[index] = theta[index] + change_w
				theta[2] = theta[2] + change_b
				#print(theta)
				return percive_machine(train_x, train_y, theta, rate)
			# return percive_machine(train_x, train_y, theta, rate)
		# change = rate*np.dot(np.transpose(train_x[:,0:2]), difference)
		# print(change)


percive_machine(train_x, train_y, theta, rate)

# a = np.array(([1],[2]))
# def aaa(n):
# 	n[1] = n[1] +1
# 	print(n)

# aaa(a)