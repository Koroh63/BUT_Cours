import numpy as np
import time

A = np.random.randint(1,10,size = (3,3))
B = np.random.randint(1,10,size = (3,3))
print(f"Matrix A:\n {A}\n")
print(f"Matrix B:\n {B}\n")
C = np.matmul(A,B)
print(f"Matrix C:\n {C}\n")
# print(len(A[0]))
# print(len(B[0]))
# print(C[2][1])

def prodMat(A,B):
    if(len(A[0]) != len(B)):
        print("error : matrice size not compatible")
        return

    [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            tmp = 0 
            for k in range(len(B)):
                tmp = tmp + (B[k][j]*A[i][k])
            C[i][j] = tmp
    return C

# print(prodMat(A,B))

def prodStrassen(A,B):
    if(len(A) == len(B) and len(A[0]) == len(B[0]) and len(B[0]) == len(B) and len(B)%2==0 ):
        
        return
    else:
        print("error : wrong matrice size")

prodStrassen(A,B)

L=[4,1,13,-4,16,2,14,14]
print(L.index(14))

def triSelect(List):
    for i in range(len(List)):
        m = min(List[-(len(List)-i):])
        if(List[i]!=m):
            List[len(List) - 1 -List[::-1].index(m)]=List[i]
            List[i] = m

    return List

L1= list(np.random.randint(1,10,size = 5000))

start = time.time()
L1 = triSelect(L1)
end = time.time()
elapsed = end - start
print(L1)
print(elapsed)
