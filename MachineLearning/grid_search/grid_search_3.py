#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/9 13:09
@description：分训练集，验证集和测试集，并进行交叉验证
"""
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
iris = load_iris()
X_train_val, X_test, y_train_val, y_test = train_test_split(iris.data, iris.target, random_state=0)
X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, random_state=1)
print("Size of training set:{} size of validation set:{} size of testing set:{}".format(X_train.shape[0],
                                                                                       X_val.shape[0], X_test.shape[0]))
best_score = 0.0
for gamma in [0.001, 0.01, 0.1, 1, 10, 100]:
    for C in [0.001, 0.01, 0.1, 1, 10, 100]:
        svm = SVC(gamma=gamma, C=C)
        # 5折交叉验证
        scores = cross_val_score(svm, X_train_val, y_train_val, cv=5)
        # 取平均数
        score = scores.mean()
        if score > best_score:
            best_score = score
            best_parameters = {"gamma": gamma, "C": C}
svm = SVC(**best_parameters)
svm.fit(X_train_val, y_train_val)
test_score = svm.score(X_test,y_test)
print("Best score on validation set:{:.2f}".format(best_score))
print("Best parameters:{}".format(best_parameters))
print("Score on testing set:{:.2f}".format(test_score))
