from numpy import *
import numpy as np
import operator
import collections

def createDataSet():
    group = array([[2.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    #shape[0] return the number of collumns of dataset
    dataSetSize = dataSet.shape[0]
    #repeat the vector with times of dataSetSize in the row direction
    #repeat the vector with times of 1 in the collumn direction
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    #calculate the square of the subtraction
    sqDiffMat = diffMat**2
    #sum meas the sum of all the elements 0 will sum all the rows 1 will sum all the collumns
    sqDistances = sqDiffMat.sum(axis=1)
    #calculate the square root and obtain the distance
    distances = sqDistances**0.5
    #return the index of the distance after sort by ascending order
    sortedDistIndices = distances.argsort()
    print(sortedDistIndices[0])
    #create an dictinary to contain the frequencies of labels
    classCount={}
    for i in range(k):
        #get the k-th label
        voteILabel=labels[sortedDistIndices[i]]
        #use the dictionary to save the frequency
        classCount[voteILabel]=classCount.get(voteILabel,0)+1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    
    return sortedClassCount[0][0]
