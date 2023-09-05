# Nouveaux Paradigme de BDD

### **Utilisation de 2 techniques dans les architectures des BDD distribuées** : 
- Réplication 
- Partage 

# Réplication du serveur en plusieurs fois pour des besoins de sécurité :
Avec ses avantages et désavantages .

## Mise à jour des modifications de 2 façons : 
- **Synchrone** : immédiat, petit fenêtre d'incohérence, occupation de la base par la propagation constante des modifications
- **Asynchrone** : intervalles réguliers, plus d'incohérence mais moins d'occupation

## Types d'architechture de réplication : 
- **Maitre / esclaves** 
 : Seul le master recoit les modifs et envoi aux slaves qui peuvent êtres lues 

- **Peer to Peer** : tout le monde peut écrire sur tout le monde : prblm de conflit possible

# Partage ( Sharding )

Séparation des données par bloc de 128Mo ( facteur de réplication pris en compte)

# Consistence des architectures
On doit faire attention à la consistence de la bdd aux travers des serveurs ( replica ou transactionnel )

Les bdd relationnelles privilégient la cohérence plutôt que la disponibilité tandis que
Le NoSQL lui a plus de liberté : BASE 

## **Théorème CAP** : Consistency Availability Partition tolerence
On peut pas avoir les 3 propriétés en même temps 

## CP (consistency and partition tolerence) : 
- relationnelles et NoSQL ( MongoDb, CouchDb, Redis, HBse)
## AP (accessibility and partition tolerence) : 
- Base de données NoSQL ( Cassandra, DynamoDb)

### **Les données peuvent être classifiés en 4 types :**

- Données structurés : modèle prédéfini 
- Données non-structurées : Fichier video, binaires, images
- Données dynamiques 
- Données statiques 