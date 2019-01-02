from sklearn import datasets 
from sklearn import svm
from sklearn .model_selection import train_test_split

wine = datasets.load_wine()

features = wine.data 
labels = win.target

print "Number of entries: ", len(features)
for featurename in wine.feature_names:
    print featurename[:10], "   \t",
print "Class"
for feature, label in zip(features, labels):
    for f in features: 
        print f, "\t\t",
    print label

train