

L=[1,2,5,10,20,50,100,200,500]

def MonnaieRec(n,L):
    if (n in L):
        return 1
    min_coins = float('inf')
    for d in L:
        if n - d >= 0:
            num_coins = 1 + MonnaieRec(n - d, L)
            min_coins = min(min_coins, num_coins)

    return min_coins




# UUID=5b9bd882-047b-4894-b16e-1b42e00b28b3

def MonnaieProgDyn(n, L):


    valeurs[0] = 0
    
    for i in range(1, n + 1):
        for j in range(len(L)):
            if i - L[j] >= 0 :
                valeurs[i] = min(valeurs[i], valeurs[i - L[j]] + 1)
    return valeurs[n]

print(MonnaieProgDyn(37,L))
print(MonnaieRec(37,L))