#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/5/10 21:35
"""
from sklearn.model_selection import ShuffleSplit
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from collections import defaultdict
from sklearn.datasets import load_boston
import numpy as np
boston = load_boston()
X = boston["data"]
Y = boston["target"]
names = boston['feature_names']
rf = RandomForestRegressor()
scores = defaultdict(list)

# crossvalidate the scores on a number of different random splits of the data
for train_idx, test_idx in ShuffleSplit(random_state=0).split(X):
    X_train, X_test = X[train_idx], X[test_idx]
    Y_train, Y_test = Y[train_idx], Y[test_idx]
    r = rf.fit(X_train, Y_train)
    acc = r2_score(Y_test, rf.predict(X_test))
    for i in range(X.shape[1]):
        X_t = X_test.copy()
        np.random.shuffle(X_t[:, i])
        shuff_acc = r2_score(Y_test, rf.predict(X_t))
        scores[names[i]].append((acc - shuff_acc) / acc)
print("Features sorted by their score:")
print(sorted([(round(np.mean(score), 4), feat) for feat, score in scores.items()], reverse=True))
