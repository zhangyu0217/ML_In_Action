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
# Disadvantage
