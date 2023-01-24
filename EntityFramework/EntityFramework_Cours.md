# Entity Framework

### Eval

##### Conception
Plusieurs clients mobiles, web et desktop et le model est le même pour tous fonctionnant en local et pouvant consommer une BDD (partie Entity Framework). Sur un côté distant on veux aller cherhcher ses données via une web API qui consomme lui aussi une bdd (Conso de Service).

Le client, la logique, le modèle et le stub sont fournis

##### Objectif :
- Construction et consommation de la BDD avec EF core
- puis avec un client spécifique pour pouvoir dialoguer avec l'API
- Rajouter un couche d'abstraction( Stratégie ) pour que les consommations soit interchangeables.
- Gérer les bases, les tables et l'évolution
- Déployer l'application
- Rajouter de la qualité (tests)

##### Exercice 

10 points :
- Ex 1: 1 BDD avec 1 table champion puis on l'utilise par le client avec des requêtes CRUD + du filtrage
- Ec 2 : test unitaires avec bdd stubé avec SQLiteinMemory pour tests
- Ex 3 : Déploiement et tests (code firsts) 

6 points :
- Ex 4 : Même chose avec rune et skins en 1 table (3 tables séparés)
- Ex 5 : Relation entre champion et skin (1 to many) ()
- Ex 6 : Relation entre chmapion page de rune et rune (2 fois many to many)

4 points :
- Ex 7 : Mapping entre modèles et entité (qualité) :
    - part 1: 1 tables (after 5)
    - part 2: relations (after 6)
- Ex 8 : Rajouter le pattern Unit of work ( permet de faire un rollback )

## Partie 1 :

**EF core** : c'est un ORM (Object Relationnal Manager)
créer bases, tables et fais la partie requêtes ()

-Fonctionnement-

Il va d'abord créer la base en utilisant une classe fille dérivée de DBContext et de la méthode onconfiguring():
- Quel fournisseur vous choisissez (On ne choisit pas) : on lui passe juste le SGBD en param ( via nuget ) c'est EF qui fait la liaison(permet de faire la liaison ), mais impossible de faire des méthodes spécifique à un sgbd

Onconfiguring s'occupe de créer la base 


La classe fille possède une collection sous forme de DBSet de 
L'entité permet d'encapsuler des propriétés qui seront stockés dans des tables et est assez malin (donc automatismes) mais on peut rajouter des contraintes

2e partie : client qui utilise db context pour faire des requetes et obtenir des collections d'entité grâce à link to entities( permet de faire des requetes sur des collections : nounours.where(n=> n.nbPoils>500).orderBy(n=>n.id), where , take, select, slect many, order by )

