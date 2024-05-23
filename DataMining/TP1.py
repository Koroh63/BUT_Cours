import numpy.random as random
import matplotlib.pyplot as plt
import numpy as np

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

vector = random.randint(0,10,size=1000)
# print(myMean(vector=vector))
# print(myMode(vector=vector))
# print(myMedian(vector=vector))
# print(myDefDomain(vector=vector))
# print(myStandartDeviation(vector=vector))
# print(myVariance(vector=vector))

# EXO 2 
print("--- EXO 2 ---")
yB = [10,12,48,23,24,48,9,7,13]
xB = [5,8,9,10,11,12,13,14,16]
print("Effectif :   "+ str(yB))
print("Valeur :     "+ str(xB))

# plt.bar(xB,yB)
# plt.show()

vector = tabToList(xB,yB)
print(' - Tendance Centrale :')
print("Mode :       "+str(myMode(vector)))
print("Median :     "+str(myMedian(vector)))
print("Mean :       "+str(myMean(vector)))
print(' - Dispersion : ')
print('DefDomain :  '+str(myDefDomain(vector)))
print('MeanDeviation:'+str(myMeanDeviation(vector)))
print('Variance:    '+str(myVariance(vector)))
# Exercice 3
QI = np.random.normal(100, 225**0.5, 100000)

print(QI)
# plt.hist(QI, 30, density=True, alpha=0.5,)
# plt.show()

print(myMean(QI))
print(myVariance(QI))

n = np.count_nonzero(QI<60)

print(str((n/100))+"%")
