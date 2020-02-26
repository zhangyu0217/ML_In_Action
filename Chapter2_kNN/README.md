# What is kNN?
  kNN means the k-nearest neighbouring. It is a supervised machine learning method.
# Strategy
+ A sample is given. Each event is a N-dimension vector and the the label is given.
+ Calculate the distance between the event of each given training sample and the test event.
+ Collect the k leading events in the given training sample.
+ Calculate the frequency of each labels in the collection.
+ The most frequent label is the result of classification.
# Opimization&Implementation
+ The size of training sample and the quantity of k.
+ The key of the implementation is to build a vector for each event.
+ Acatually a general IO systema could be build.
+ Input : JSON file containing training sample
+ Output : the k leading events and the result. It is perfect if there is a visualization.
# Advantage
+ Easy for understanding and implementation.
+ No need to know the model or distribution of different labels
+ Not sensitive to the exotic event.
# Disadvantage
+ Computational complexity grows up when the dimension grows up.
# Personal understanding
+ This method is no more effective than rectangular cut method or decision tree.
+ Because it almost selects a sphere around the test event and count the fequency of labels  
+ This method treats all the dimensions equal, so we do not know which dimension is the most significant.
+ <span style="color:red">Question</span>: What is the boundary of the classfication for a give sample?
+ $\color{red}{test}$
