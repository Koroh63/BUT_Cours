import numpy.random as random
import matplotlib.pyplot as plt
import numpy as np

def myMean(vector):
    return sum(vector)/len(vector)

def myMode(vector):
    return np.argmax(np.bincount(vector))

def myMedian(vector):
    if(len(vector%2==1)):
        return sorted(vector)[(len(vector)//2)+1]
    return (sorted(vector)[len(vector)/2]+sorted(vector)[(len(vector)/2)+1])/2

def myDefDomain(vector):
    return max(vector)-min(vector)

def myStandartDeviation(vector):
    avg = myMean(vector=vector)
    v2 = lambda x:(x-avg)**2
    return (sum(v2(vector))/len(vector))**0.5

def myVariance(vector):
    return myStandartDeviation(vector=vector)**2

vector = random.randint(0,10,size=1000)
# print(myMean(vector=vector))
# print(myMode(vector=vector))
# print(myMedian(vector=vector))
# print(myDefDomain(vector=vector))
# print(myStandartDeviation(vector=vector))
# print(myVariance(vector=vector))

B = [[5,10],[8,12],[9,48],[10,23],[11,24],[12,48],[13,9],[14,7],[16,13]]

x_values = [sublist[0] for sublist in B]
y_values = [sublist[1] for sublist in B]

# Exercice 3
QI = np.random.normal(100, 225**0.5, 100000)

print(QI)
# plt.hist(QI, 30, density=True, alpha=0.5,)
# plt.show()

print(myMean(QI))
print(myVariance(QI))

n = np.count_nonzero(QI<60)

print(str((n/100))+"%")
