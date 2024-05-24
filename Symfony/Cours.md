# Symfony

## Partie 1 : Introduction  

Interêts du FrameWork :
-  + rapide
-  + organisé 
-  + sécurisé

Modèle MVC ( Modèle - Vue - Controlleur )

### Structure

Principaux :
- config/ : routes, services et packages
- src/ : code
- template/ : front Twig

Autres :
- bin/ les binaire
- var/ stockage des fichiers générés
- vendor/ tiers des librairies
- public/ racine du site

### Bundles et Packages 

Composer est le gestionnaire de package PHP  
-> Général à PHP mais pas spécialement pour Symfony

    symfony composer require "package" (--dev)

Bundles Symfony gestionnaire de  Symfony
-> Spécifique à Symfony : les package doivent être enregistrés dans App.kernel

### Jeux de test 

Types :
- Unitaires : méthodes, paramètres
- Intégration : ajout dans un projet -> Niveau Controller
- Fonctionnel : validation du comportement
- Autres : robustesse, performance, ergonomie, ...

Outils : 
- TestCase : Unitaire PHP
- KernelTestCase : Basic pour Symfony
- WebTestCase : Execution des scenario sans JS 
- APITestCase : Orienté API 
- PantherTestCase : Utilisation End 2 End avec un vrai browser
    
    
    symfony php bin/phpunit


## Partie 2 : Routes 


### Définition des routes 
Utilisation d'attributds PHP pour les routes -> PHP8
Annotations -> <PHP8

Définition dans un fichier annexe (en YAML : ***config/routes.yaml***)

### Paramétrage des routes 
- **methods** : Resteindre les routes en fonction du type d'appel
- **condition** : Encore plus de condition pour restreindre *
- **requirements** : définit les formats des paramètre
- **($var = 1)** : définit des paramètres par défaut
- **priority** : Définir l'ordre de priorité

##### **Les groupes de routes :**

Annotations de route sur le controlleur permet de groupe les routes à l'intérieur qui auront toutes la même route de début et les mêmes paramètres de base

### Débug des routes
Pour déboguer les routes : 
- symfony console debug:router ( list les routes )
- symfony console router:match /blog/post/8 ( test la route )

### Fonctions des routes 

Récupération des paramètres et du nom de la route dans des variables 
Redirection de la route en fonction des paramètre
Génération des URLs possible et de la gestion des paramètres aussi

## Services et Injections de dépendances 

Objet PHP effectuant des tâches spécifiques /src
Le conteneur de service va gérer le service 

Utilisation du service en injection de dépendances:
    -> AutoWiring  : Symfony instancie les managers lui-même en utilisant la configuration dans services.yaml

    symfony console debug:container -> liste les services autowiré

Configuration manuelle des paramètres toujours possbile cependant

## Partie 3 : BDD 

Utilisation de l'ORM **Doctrine** ( installation via composer ) et Liaison avec la BDD via la variable DATABASE_URL dans le .env (chemin ou addresse)

Afin de générer la classe correspondant aux tables : 

    symfony console make:entity

Et ensuite création de la table par migration :

    symfony console make:migration -> génère le fichier php avec les infos 
    symfony console doctrine:migration:migrate -> applique les changements 

Dans le controller, faire des new et utiliser la commande persist pour enregistrer en BDD cet objet et utilise flush pour commit le tout 

    $entityManager->persist($produit);
    $entityManager->flush()

A la création de l'entité, le repository lié est créé aussi afin de gérer les collections de ces objets : 
- find ($id)
- findOneby (['name' => 'Nom'])
- findBy
- findAll

Pour des requêtes plus complexes : créer des méthodes personnalisées.

## Partie 4 : Twig

Générateur de code HTML, CSS, etc

    {{ ... }} : affichage contenu de variable ou résulta d'une expréssion 
        - path pour rediriger vers une route du controller
        - asset pour générer l'url des assets statique
        - variable apps
    {% ... %} : logique (condition ou boucle )
    {# ... #} : commentaires 

Inclusion et héritages des templates Twig 

### TD : 

    #[ORM\Entity]
    class Personne
    {
        #[ORM|Id]
        #[ORM\GeneratedValue]
        #[ORM|Column(type: 'integer')]
        private int $id

        #[ORM\Column(type: 'string')]
        private string $prénom

        #[ORM\Column(type: 'integer')]
        private string $age

    }


    {% for personne in personnes %}
        {% if personne.age >=  0 and personne.age < 25 %}
            {{ personne.name }}
        {% endif %}
    {% endfor %}


# Sécurité 

### Man in the middle (ARP Spoofing)
Interception et alteration des communications entre 2 tiers 

#### Prévention 
- Chiffrement : HTTPS/TLS pour sécuriser le transit
- Certificats : vérifier et éviter les non-fiables 
    -> Configurer le Virtual Host ( apache ou nginx au niveau du serveur)
    -> Activation du security-bundle , redirection du http vers https ou dans apache directement 

### Cross-Site-Scripting
Injection de code dans les pages de vues

#### Prévention 
- Echappement de données 
    ->symfony/html-sanatize 
- Politique de sécurité : implémenter des CSP pour limiter les sources de XSS

### Inclusion de Fichier Locaux / à Distance
Accès non-autorisés à des fichiers sensibles 

#### Prévention
- Validation d'entrée : restreindre les chemins 
- Désactivation des inclusions dynamiques 
- Désactiver allow_url_include & allow_url_fopen

### Injection SQL

#### Prévention : 
- Echappement des entrées
- Requêtes préparées 
- ORM sécurisé ( Doctrine )
- Gestion des erreurs 

### Cross-Site-Forged-Request

#### Prévention 
- Tokens anti-CSRF 
- Attributs SameSite dans les cookies 
- En-tête Referer pour domaines autorisés 

### Problèmes d'authorisations sur le site 

#### Prévention 

Contrôle d'accès strict basé sur les rôles RBAC
Sessions sécurisées et gestion robuste des identifiants
Test de pénétration


## Formulaires 

composer require symfony/form