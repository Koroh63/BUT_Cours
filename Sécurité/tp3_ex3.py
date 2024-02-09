global password
import time

def checkpassword(l):
    for i in range(len(password)):
        time.sleep(1)
        if password[i]!= l[i]:
            return(False)

    return(True)

password=input("L’ordi va deviner votre code PIN de chiffres entre 0 et 9 de longeur 6 : ")

def cracker():
    passa=['0','0','0','0','0','0']
    for j in range(6):
        for k in range(9):
            print ('trying : ',''.join(passa))

            start = time.time()
            if(checkpassword(''.join(passa))==True):
                print('Password is :',''.join(passa))
                return
            end = time.time()
            print(end - start)
            if(end - start > 2 + j):
                break
            passa[j]=str(1+int(passa[j]))

cracker()