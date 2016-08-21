from sklearn.naive_bayes import GaussianNB
def classify(features_train, labels_train):
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier


    ### your code goes here!
    clf = GaussianNB()
        ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)

    return clf

def accuracy(features_train, labels_train):
    clf = classify(features_train, labels_train)

    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example,
    ### where we just print the accuracy
    ### you might need to import an sklearn module
    accuracy = clf.score(features_train, labels_train)

    return accuracy
