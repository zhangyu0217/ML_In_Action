from numpy import *
import numpy as np
import operator
import collections

def createDataSet():
    group = array([[2.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    #calculate the distance
    dist = np.sum((inX - dataSet)**2, axis=1)**0.5
    #obtain the k-nearest label
    k_labels = [labels[index] for index in dist.argsort()[0 : k]]
    #count the frequency of labels
    label = collections.Counter(k_labels).most_common(1)[0][0]
    # return the most frequent label
    return label
