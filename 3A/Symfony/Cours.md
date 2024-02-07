# Symfony

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

Objet PHP effectuant des tâches spécifiques 
Le conteneur de service va gérer le service 

AutoWiring  : Symfony instancie les managers lui-même 

Configuration manuelle des paramètres toujours possbile cependant

## Partie 3 : BDD 

Utilisation de l'ORM **Doctrine** ( installation via composer ) et Liaison avec la BDD via la variable DATABASE_URL dans le .env (chemin ou addresse)

Afin de générer la classe correspondant aux tables : 

    make entity

Et ensuite création de la table par migration :

    symfony console make:migration -> génère le fichier php avec les infos 
    symfony console doctrine:migration:migrate - applique les changements 

Dans le controller, faire des new et utiliser la commande persist pour enregistrer en BDD cet objet et utilise flush pour commit le tout 

A la création de l'entité, le repository lié est créé aussi afin de gérer les collections de ces objets : 
- find ($id)
- findOneby (['name' => 'Nom'])
- findBy
- findAll

Pour des requêtes plus complexes : créer des méthodes personnalisées.

## Partie 4 : Twig

Générateur de code HTML, CSS, etc

    {{ ... }} : affichage contenu de variable ou résulta d'une expréssion 
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