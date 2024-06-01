import numpy.random as random
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import streamlit as sl
import sklearn.preprocessing as pre
import pandas as pd

import scipy.stats as scp

from sklearn.datasets import load_iris

def myMean(vector):
    return sum(vector)/len(vector)

def tabToList(values,effectif):
    if(len(values)!=len(effectif)):
        return
    vector = []
    for i in range(len(values)):
        for j in range(effectif[i]):
            vector.append(values[i])
    return vector

def myMode(values):
    modes = []
    for value in values:
        if modes==[] or values.count(value)>values.count(modes[0]):
            modes=[value]
        else:
            if values.count(value)==values.count(modes[0]) and not value in modes:
                modes.append(value)
    return modes

def myMedian(vector):
    if(len(vector)%2==1):
        return sorted(vector)[(len(vector)//2)+1]
    return (sorted(vector)[len(vector)//2]+sorted(vector)[(len(vector)//2)+1])/2
   
def myMeanDeviation(vector):
    mean = myMean(vector)
    return(myMean([abs(x-mean) for x in vector]))

def myDefDomain(vector):
    return max(vector)-min(vector)

def myStandartDeviation(vector):
    avg = myMean(vector=vector)
    v2 = lambda x:(x-avg)**2
    return (sum(v2(vector))/len(vector))**0.5

def myVariance(vector):
    return myStandartDeviation(vector=vector)**2

def myCorrelation(v1,v2):
    return myCovariance(v1,v2)/(myStandartDeviation(v1)*myStandartDeviation(v2))

def myCovariance (v1,v2):
    sum = 0
    moy1 = myMean(v1)
    moy2 = myMean(v2)
    for i in range(len(v1)):
        sum += (v1[i]-moy1)*(v2[i]-moy2)
    return sum/len(v1)

iris = load_iris()
data1 = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])
# print( data1.columns)

sepal_length = data1['sepal length (cm)']
sepal_width = data1['sepal width (cm)']
petal_length = data1['petal length (cm)']
petal_width = data1['petal width (cm)']
target = data1['target']

# plt.figure(figsize=(12, 8))

# plt.subplot(2, 3, 1)
# plt.hist(sepal_length, bins=20, color='b', alpha=0.7)
# plt.title('Sepal Length (cm)')

# plt.subplot(2, 3, 2)
# plt.hist(sepal_width, bins=20, color='g', alpha=0.7)
# plt.title('Sepal Width (cm)')

# plt.subplot(2, 3, 3)
# plt.hist(petal_length, bins=20, color='r', alpha=0.7)
# plt.title('Petal Length (cm)')

# plt.subplot(2, 3, 4)
# plt.hist(petal_width, bins=20, color='y', alpha=0.7)
# plt.title('Petal Width (cm)')

# plt.subplot(2, 3, 5)
# plt.hist(target, bins=3, color='purple', alpha=0.7)
# plt.title('Target')

# plt.tight_layout()
# plt.show()


# print(myCorrelation(sepal_width,sepal_length))
# print(myCorrelation(sepal_width,petal_length))
# print(myCorrelation(sepal_width,petal_width))
# print(myCorrelation(sepal_length,petal_length))
# print(myCorrelation(sepal_length,petal_width))
# print(myCorrelation(petal_length,petal_width))

# print(sepal_width.corr(sepal_length))
# print(sepal_width.corr(petal_length))
# print(sepal_width.corr(petal_width))
# print(sepal_length.corr(petal_length))
# print(sepal_length.corr(petal_width))
# print(petal_length.corr(petal_width))

# dataCorr = data1.corr()
# print(dataCorr)

# sepal_width_sepal_length_interval = scp.norm.interval(0.95, loc=dataCorr.mean(), scale=dataCorr.std())
# print( sepal_width_sepal_length_interval)

# plt.plot(np.reshape(sepal_width_sepal_length_interval,[2,5]))
# plt.show()

from sklearn.decomposition import PCA

tab = pd.read_csv("bats.csv",delim_whitespace=True)
tab_excl_species = tab.drop(["Species","id","Diet"],axis=1)
print(tab_excl_species)

