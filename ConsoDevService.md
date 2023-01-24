# Consommation et Développement de services : Cours 

### Evaluation

Projet commun avec Marc Cheval
"Grille notation"
#### API
#### API Gateway



## Partie 1 
Qu'est ce qu'une API : Application Programming Interface, Exploiter des ressources distantes 

API Rest 

URI : Uniform Ressource Identifier, url + urn 
Protocol Http 

Rest : Representationnal State Transfer
Stateless : Pas de session : utilisation de token 
pas d'affichage : client 
Layered : intermédiaires non-visibles rendre possbile les surcouches 
Verbes : 
GET : récup 
POST : Création
PUT : Mise à jour
DELETE : Supp

Codes de retours : 
100 informations
200 succès
300 retours
400 erreurs coté client
500 erreurs serveurs 

Richardson Matury Model higher level better grade
Niveau 0 : RPC HTTP
Niveau 1 : segmentation en ressource
Niveau 2 : utilisation des verbes et des codes de retours : Savoir
Niveau 3 : utilisation des controles hypermedia 

> utiliser rider de jetbrains : .net 6


créer projet 
API web asp.net core c#
activer https, docker, controllers ,open api
