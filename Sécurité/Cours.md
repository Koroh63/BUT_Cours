# **Sécurité** 

Sujets de présentations : 

- TLS (5) : CRIME
- HARDWARE/IOT (5) : ShellShock
- Autre : OSINT

avant le 26 sept : nom du presentateur en amphi  
2 oct avant 22h : slide de la présentation de 3 min  
minuit avant le td : slide de la pres de td  
minuit avant le tp : sujet + correction par mail 

# Part 1 : Fonctionnement du web 

http/html & ip tcp/udp 

- navigateurs 
- protocols 
- languages 

ssllabs -> analyse la qualité de l'url 

# Part 2 : RGPD  
- Désigner un Délégué à la protection des données 
- Cartographier les données personnelles et leur flux (Registre de traitements)
- Prioriser les données 
- Gérer les risques 
- Organiser, sensibiliser et anticiper les violations 
- Documenter 

# Part 3 : Attaques 

## XSS : Cross Site Scripting

Injection de code via une page web  : utilisation d'un formulaire pour écrire un bout de code JS qui s'exécute
 - Mettre en Blind pour que l'attaquant ne voit pas le résultat

Processus : phish, click collect and leak pour exécuter le script sur le serveur et récupérer les informations
Persistant : publish, click, collecte and leak : attaquant ecris sur le serveur, la victime clique dessus etexécute le script de collecte.
DOM Document Object Model : c'est la victime qui exécute la fonction

- Pour contrer, éviter les formulaire et particulièrement ceux qui écrivent sur le serveur 
- Validation stricte des entrées 
- WAF web application firewall 
- définir les mécanismes de sécurité

## CSRF Cross site request forgery ou XSRF: 

Envoyer un accès à un site à la victime avec le même navigateur que celui déjà ouvert pour récupérer les cookies d'auth vers les pages sensibles ciblées.

## SSRF Server Site request forgery :


## LFI / RFI 

Insertion de fichier malicieux locaux ou distants sur les pages ( include )
-> retirer les php.ini et filtrer les urls 

## nmap et ssh audit 

## RCE : Remote code execution

# Présentations : 

### Heart Bleed : 
TLS - Avril 2014 - OpenSSL

Accès à des données privées ou sensibles, repose sur la fonction heartbeat 
Le hacker fait une requête avec un poids plus conséquent 

### WEP & WPA
Wifi - 2000/1999 - 

Chiffrement Déchiffrement 
WEP vulnérable car clé courte donc passage à WPA -> protocole de chiffrement 

### Spectre 
Attaque sur le CPU ( n'importe quel proc) 
permet d'accéder au cpu cache et récupérer les informatinos stocker dedans et notamment les secrets

### Type Juggling / Request smuggling

type juggling : Fonstion php non-typé, si le hash commence par 0e -> la comparaison avec 0 retourne toujours true (connexion) , on peut forcer la comparaison 
Smuggling : Si http 1 ou 1.1 : Le serveur front-end interprète la requete differement que le back-end mais esr le seul a la vérifier -> faille 

### ARP Spoofing / DNS poisoning 

### Freak + LogJam

### Poodle 
TLS / SSL 3.0 -> Retrograder la version de la machine vers SSL 3 
Bourrage de donnée sur Oracle : pour trouver le IV et donc obtenir le message initial 

### ShellShock 
2014 - Faille du shell unix 

Injection de commandes shell dans des variables qui peuvent être utilisées -> patch 