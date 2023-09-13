# Sécurité TP1 

# Exercice 1 :

# **Ex: 1** 

1. Nous pouvons observer que sur le fichier berlin_http, qui represente les dumps entre differentes IPs en HTTP, nous pouvons comprendre et voir facilementles informations qui sont communiqués entre les deux serveur. Par exemple, on sait que le client 192.168.105.141 a envoyé une requete POST vers le serveur 192.168.128.30, et que le serveur a repondu avec un OK (code 200) et qu'il a renvoyé un text/html.

Cependant, sur les dumps du fichier berlin_https, nous ne voyons pas ces informations. On comprend que le client 192.168.105.141 se connect sur le serveur 192.168.128.30, avec un échange de message "Client Hello" et "Server Hello", mais après cela les deux IPs font un "Encrypted Handshake Message", ce qui leur permet de se donner des informations encryptés, que seulement eux comprennent. Il est donc impossible de comprendre, juste en regardant les dumps, les informations qui sont communiqués entre ce client et ce serveur. HTTPS permet donc un échange plus sécurisé que HTTP.

2. Grâce à Wireshark, nous pouvons voir que quand nous tentons de nous connecter sur le site avec des logins et mots de passe factice, nous éméttons une requête vers le serveur qui nous renvoie ensuite une réponse, cryptée en HTTPS.
Cependant, étant en HTTPS, nous ne pouvons pas decrypter les informations qui circulent entre le client, nous et le serveur.


# Exercice 2 

# **Lettre 0** : 
le mot de passe et le login étant les mêmes et correspondant au prénom présent à la fin de la lettre : Pascal ( avec la casse )
- Login : Pascal 
- Mdp : Pascal

# **Lettre 1** : 
On peut tester chaque chiffre un à un jusqu'à trouver celui qui affiche vert, cependant on peut éliminer un essai à chaque chiffre du code car après avoir tester 9 possibilité on sait que la 10ème est correcte donc : 9 + 9 + 9 + 10 (il faut rentrer le code à la fin)
- Login : Pascal 
- Mdp : 37

# **Lettre 2** : 
Pour trouver le déchiffré du chiffré il a fallu d'abord analyser le schéma et obtenir les formules suivantes : 
- Y1 = X4 + K3 + K5
- Y2 = X2 + K2 + K6
- Y3 = X1 + K4 + K7
- Y4 = X3 + K1 + K8

Grâce à ces formules et à l'utilisation du chiffré/déchiffré que nous as donné Eli on a pu détrminer les valeurs des couples de K :
- 7 = 3 + K3 + K5 -> K3 + K5 = 4
- 4 = 1 + K2 + K6 -> K2 + K6 = 3
- 6 = 0 + K4 + K7 -> K4 + K7 = 6
- 8 = 2 + K1 + K8 -> K1 + K8 = 6

On a pu donc inverser la formule pour l'utiliser afin de retrouver les X : 
- X4 = Y1 - 4
- X2 = Y2 - 3
- X1 = Y3 - 6
- X3 = Y4 - 6

Avec le chiffré [3,4,5,3] on obtient le Mdp 9179

- Login : Pascal  
- Mdp : 9179

# **Lettre 3** : 
Afin de trouver les 2 bases par lesquelles est passé le général il a fallu déterminer d'abord le temps de vol de l'avion mais attention au décalage horaire : le vol de 30 min devient 1 h et 30 min et celui de 2 h et 42 min devient 1 h 42 min.

On peut ensuite déterminer la distance parcourue lors des vols avec le modèle de l'avion :
- vol 1 : 1,7 * 160 = 272 miles
- vol 2 : 1/3 * 160 = 53 miles
- vol 3 : 1,5 * 160 = 240 miles 

On peut alors déterminer sur la carte les bases car il y a :
- 272 miles entre Rabaul et Ballale
- 53 miles entre Buin-Faisi et Ballale
- 240 miles entre Buin-Faisi et Rabaul

Les 2 bases sont donc Buin-Faisi et Ballale

- Login : Pascal   
- Mdp : BALLALEBUIN-FAISI

# **Lettre 4** : 

On a quelques informations sur le dechiffrement. Tout d'abord, on connait P1, P3 ainsi que C4, qui est égal à P3. On peux alors poser différentes équations. On a donc :

C'1 = P'1 ⊕ C'0
C'2 = P'2 ⊕ C'1
C'3 = P'3 ⊕ C'2
C'4 = P'4 ⊕ C'3

On connait C'4, donc C'4 = 1000 1001 1011.
On sait aussi que C'k = Ck-2, avec k>= 4. L'énoncé nous dit que l'on peut modifier seulement les deux premiers blocs chiffrés impaires. Par conséquent C2 = C'2, et C2 = C'4. On a par conséquent l'équiation suivante : 

C'3 = P'3 ⊕ C'2, donc C'3 = 1000 1001 1011 ⊕ 1000 1001 1011 = 0000 0000 0000

Donc on a maintenant C'3 = 0000 0000 0000
On a de nouveaux nos différentes équations, mais maintenant avec les différents valeurs que nous avons trouvé et qui nous sont fournies :

C'1 = 0111 1111 0111 ⊕ C'0
1000 1001 1011 = P'2 ⊕ C'1
0000 0000 0000 = 1000 1001 1011 ⊕ 1000 1001 1011
1000 1001 1011 = P'4 ⊕ 0000 0000 0000

Avec C'0 = IV', nous devons trouver le resultat décimal de C'0 ⊕ C'1 ⊕ C'2 ⊕ C'3 ⊕ C'4

En remplacant par les valeurs que nous connaissont déjà, nous avons donc :

C'0 ⊕ C'1 ⊕ 1000 1001 1011 ⊕ 0000 0000 0000 ⊕ 1000 1001 1011

Donc 

C'0 ⊕ C'1 ⊕ 1000 1001 1011 ⊕ 1000 1001 1011

Donc

C'0 ⊕ C'1 ⊕ 0000 0000 0000

Donc au final il nous reste seulement C'0 ⊕ C'1 à calculer, car ⊕ 0000 0000 0000 ne change rien à un ⊕.

Cependant, nous avons C'1 = P'1 ⊕ C'0, et il est possible, avec les XOR, de trouver toute les valeurs d'une équations en XORant toute les valeurs avec les autres, par exemple si on a x=y⊕z, on a aussi y=x⊕z, et z=y⊕x. 

Donc on a P'1 = C'0 ⊕ C'1, et on connait P'1, donc C'0 ⊕ C'1 = 0111 1111 0111

Nous avons donc notre resultat final, IV' ⊕ C'1 ⊕ C'2 ⊕ C'3 ⊕ 1000 1001 1011 = 0111 1111 0111

En décimal cela donne donc 2039.

Login : Pascal  
Mot de passe : 2039

# Lettre 5 :

On peut déduire grâce au shéma de consommation la clé privé d'Alice : 

Le calcul du carré est plus optimisé que le calcul du produit, ce dernier représente donc un plus gros pic de consommation lors de l'exponentielle rapide. Et grâce aux informations que l'on nous donne on peut déterminer que un 1 dans la clé privé correspont à un carré suivant d'un produit et le 0 à seulement un carré.

En combinant celà on sait que 
- 0 : un pic bas
- 1 : un pic bas puis un pic haut 

En analysant le graphe sur les 14 bits de la clé, on obtient 00 0010 1101 0000 -> 720 en décimal

Login : Pascal  
Mot de passe : 720

# Lettre 6 :

On peut découvrir le message M de Alice et Bob :

On sait que pour chiffrer M, ils ajoutent K à M et obtiennent C, on a alors :
     
- M + Ka = 6 222 556 
- M + Kb = 1 569 560
- M + Kb + Ka = 4 658 212

On peut alors déduire : M = M + Kb - [(M + Kb + Ka) - (M + Ka)]  
En remplacant les valeurs on obtient donc 
    
    M = 1 569 560 - (4 658 212 - 6 222 556) = 3 133 904

Login : Pascal  
Mot de passe : 3133904

# Lettre 7 :

En utilisant les coordonnées trouvés au cours des exercices, nous obtenons les point suivants:
- A (17,2039)
- B (37,9179)
- C (720, 3 133 904)

On obtient alors les equations suivantes :

- 3 133 904 = a * 720² + b * 720 + c
- 9179 = a * 37² + b * 37 + c
- 2039 = a * 17² + b * 17 + c

3 équations / 3 inconnues le problème est donc résolvable et par résolution nous trouvons :
- a = 6 
- b = 33
- c = -256

Login : Pascal  
Mot de passe : 256

# Exercice 3 : 

Voici le classement : 

- 1 : Banque AXA : A+ et seul la force de cryptage perd 10%
- 2 : OCBC NISP : otient la note A+ avec de très bon nivaux en certificat et en support de protocoles avec une légère baisse de 10% en échange de clé et en force de chiffrement.
- 3 : home.bank : obtient la note de B causé par une faiblesse sur le support de protocoles TLS 1.0 et 1.1
- 4 : EcoBank otient la note de F avec aucun support de protocol !