#TODO
from sklearn import svm

clf = svm.SVC()
clf.fit([[0,0],[1,0],[0,1],[1,1]],[0,1,1,0])
results = clf.predict([[1,0],[1,0]])
print(results)