# Exercice 1 

### Question 1 : 
L'algorithme utiliser pour hacher et saler le mot de passe est le BSD 1 basé sur le MD5 et le salt est 'AAAA'. On peut voir que la forme haché montre l'agorithme '$1' et le salé en clair '$AAAA'.

### Question 2 :



openssl passwd -1 -salt BABA -in phpbb.txt -table | grep $1$BABA$DOzBWHNx08SgVSX/YuYvC/ -> batman
openssl passwd -1 -salt CACA -in phpbb.txt -table | grep XLWo4OqFFCYICqYrZ0y5i/ -> enigma

## Exercice 2:

1. Mot de passe choisi : "dri".

3. Le mot de passe utilisé pour forger le token est "Kad0c".



# Exercice 3 : 

En ayant modifié le code, notament avec known_plain_text, on voit apparaitre : "Bonjour, comment vas-tu ? Juste pour te dire que Pascal ne sera pas au bureau demain."

## Exercice 4:

Le mot de passe admin est "starwars".

# Exercice 5 :

### Question 1 :

gpg --full-gen-key -> on choisi le 2e pour DSA et El Gamal et on rentre les informations et on obitnent notre clé OpenPGP

### Question 2 :

gpg --list-key -> nous montres que la clé a bien été créée : 
    uid          [  ultime ] Corentin R <corentin.richard@etu.uca.fr>
    sub   elg2048 2023-09-19 [E] [expire : 2023-09-29]

### Question 3 :

On édite ensuite la clé avec les commandes : 
- fpr : affiche l'empreinte
- expire : change la date d'expiration en ajoutant 10 jours si l'on veut 
- addphoto : ajoute une photo d'identité
- addkey : créer une clé
- setpref AES192 SHA256
- save

### Question 4 : 

delkey pour supprimer la clé.

### Question 5 :

Dans le cas où la clé a été divulgé ou compromise on peut créer le certificat de révocation :
    gpg --gen-revoke

### Question 6 :
on peut exporter la clé publique : 


    gpg --export --armor 

    -----BEGIN PGP PUBLIC KEY BLOCK-----

    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
    =PoD8
    -----END PGP PUBLIC KEY BLOCK-----

## Exercice 6:

1. Il y a 62 caractères alphanumériques, donc 64 possibilités avec le - et _. Nous avons donc 64 possibilités de caratères * 8, donc 64⁸ possibilités, ce qui donne 2⁴⁸ possibilités de mot de passe. j'ai determiné cette puissance grâce au binaire. Pour avoir 64, nous avons besoin de 6 bits. Etant donné que nous avons un mot de passe de 8 caractères, nous prenons 2 puissance 6*8.

2. Sachant que nous avons 128 caractères ASCII, nous avons donc 128⁸ possibilités de mot de passe.
, ce qui donne 2⁵⁶. Comme expliqué précédamment, nous prenons pour 128 7 bits, donc la puissance de 2 est determiné par 2 puissance 7*8.

3. 2⁵⁶ est environ 250 fois plus élevé que 2⁴⁸. Par conséquent, il faudrait environ 250 jours pour trouver le mot de passe de la question 2 avec un brutforce.

4. Il faut avoir un fichier avec une grande liste de possibilités de mot de passe, et il faut comparer le hachage du mot de passe obtenu avec la liste de hachage de mot de passe qu'on a dans sa liste. Je pense que c'est la méthode la plus efficace pour brutforce le mot de passe.



# Exercice 7 : 

De nombreux mot de passe avec des hash similaires semblent indiquer Sherlock Holmes, on peut essayer de trouver alors le hash de : 
- echo -n "Sherlock Holmes" | openssl dgst -md5 -> 221c77182dcf30a5b111843244922ae5
- echo -n "Holmes" | openssl dgst -md5 -> 09d9f421fd6b551f869121b6b2941e6a
- echo -n "Sherlock" | openssl dgst -md5 -> c3e3b26d5591c7fcc326a7d399d734bb

On voit que Sherlock est le mot de passe.

## Exercice 8:

1. Pour se connecter en mode admin, il faut aller dans l'inspecteur du navigateur, aller dans l'onglet Stockage, et modifier la valeur invite par la valeur admin. Il faut ensuite actualiser la page, et vous êtes connecté en mode admin.
