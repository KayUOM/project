#Dependencies
import os
import urllib.parse
import pandas as pd
from pprint import pprint
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics


#def testData():

def trainData(X, y):

    model = MultinomialNB()
    model.fit(X, y)
    return model

def featureExtraction(data):

    vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(1,3))
    x = vectorizer.fit_transform(data)
    return x

# Label the data either malicious (1) or benign (0)
def labelData(data, label):

    data = [label for i in range(0, len(data))]
    return data

# Loads file content into an array
def loadFile(name):

    directory = os.getcwd()
    filepath = directory + "/" + name
    data = open(filepath,'r').readlines()

    result = []
    for d in data:
        d = str(urllib.parse.unquote(d))
        result.append(d)
    return result

def main():

    malicious = loadFile('malicious.txt')
    benign = loadFile('benign.txt')

    lblMalicious = labelData(malicious, 1)
    lblBenign = labelData(benign, 0)

    lblData = lblMalicious + lblBenign
    data = malicious + benign

    X = featureExtraction(data)
    y = lblData

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    model = trainData(X_train, y_train)

    prediction = model.predict(X_test)

    accuracy = model.score(X_test, y_test)
    recall = metrics.recall_score(y_test, prediction)
    precision = metrics.precision_score(y_test, prediction)
    print(accuracy)
    print(recall)
    print(precision)

main()


































































# from sklearn.feature_extraction.text import TfidfVectorizer
# import os
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.naive_bayes import MultinomialNB
# from sklearn import metrics
# import urllib.parse
#
# def loadFile(name):
#     directory = str(os.getcwd())
#     filepath = directory + "/" + name
#     data = open(filepath,'r').readlines()
#     data = list(set(data))
#     result = []
#     for d in data:
#         d = str(urllib.parse.unquote(d))   #converting url encoded data to simple string
#         result.append(d)
#     return result
#
# badQueries = loadFile('badqueries.txt')
# validQueries = loadFile('goodqueries.txt')
#
# badQueries = list(set(badQueries))
# validQueries = list(set(validQueries))
# allQueries = badQueries + validQueries
# yBad = [1 for i in range(0, len(badQueries))]  #labels, 1 for malicious and 0 for clean
# yGood = [0 for i in range(0, len(validQueries))]
# y = yBad + yGood
# queries = allQueries
#
# vectorizer = TfidfVectorizer(min_df = 0.0, analyzer="char", sublinear_tf=True, ngram_range=(1,3)) #converting data to vectors
# X = vectorizer.fit_transform(queries)
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) #splitting data
#
# badCount = len(badQueries)
# validCount = len(validQueries)
#
# lgs = MultinomialNB()
# lgs.fit(X_train, y_train)
#
# # lgs = LogisticRegression(class_weight={1: 2 * validCount / badCount, 0: 1.0}) # class_weight='balanced')
# # lgs.fit(X_train, y_train) #training our model
#
# ##############
# # Evaluation #
# ##############
#
# predicted = lgs.predict(X_test)
#
# fpr, tpr, _ = metrics.roc_curve(y_test, (lgs.predict_proba(X_test)[:, 1]))
# auc = metrics.auc(fpr, tpr)
#
# print("Bad samples: %d" % badCount)
# print("Good samples: %d" % validCount)
# print("Baseline Constant negative: %.6f" % (validCount / (validCount + badCount)))
# print("------------")
# print("Accuracy: %f" % lgs.score(X_test, y_test))  #checking the accuracy
# print("Precision: %f" % metrics.precision_score(y_test, predicted))
# print("Recall: %f" % metrics.recall_score(y_test, predicted))
# print("F1-Score: %f" % metrics.f1_score(y_test, predicted))
# print("AUC: %f" % auc)