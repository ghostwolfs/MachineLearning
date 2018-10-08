import numpy as np
# 运算符模块
import operator 


def createDataSet():
	group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels

group,labels = createDataSet()
# print(group,labels)


def classify(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX, (dataSetSize,1)) - dataSet
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	sortedDistances = distances.argsort()
	classCount = {}
	for i in range(k):
		votelabel = labels[sortedDistances[i]]
		classCount[votelabel] = classCount.get(votelabel,0)+1
	# print(classCount)
	sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
	print(sortedClassCount[0][0])
	return sortedClassCount[0][0]

classify([1,2], group, labels, 3)