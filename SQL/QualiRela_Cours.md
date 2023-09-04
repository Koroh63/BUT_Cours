# Qualité et Au-delà du Relationnel

### Evaluation 

1 Exam écrit (sous réserve de surprise)

# Conception

## **1. Méthode Merise**
*Livre à acheter*

Cahier des charges -> MCD  
Entité ( Table ) : Cycle de vie, de la naissance(embauche) à la mort(retraite)

**Associations :** 
- Non-hiérarchiques = **n max** de chaques côté 
- Hiérarchique : **1 max** d'un côté (fille) et **n max** de l'autre (mère)
    - Faible : côté fille à 0,1
    - Forte : côté fille 1,1
- Réflexives : entre des occurences de la même entité
- Ternaire (ou plus) : Reliant plus de 2 entités

#### *Exemple :*

![ MCD des fleurs ](img/Ex1.PNG )**MCD de conception de la vente de fleurs**

---

## **2. Modèle Relationnel** 

Modèle Logique des données proposé par Edgar Codd en 1969 pour fournir une vision machine / informatique

### **A - Conversion des relations hiérarchiques**
On ajoute des clés étrangères là ou la cardinalité est à 1 maximum, on prend la clé primaire de la mère et on la met dans a fille.

### **B - Conversion des relations non-hiérarchiques**
On convertit les relations en table avec les clés étrangères des 2 tables reliées et les attributs de la relation

#### *Exemple :* MLD
>VARIETE(numero, nom, categorie, exposition, distMinPlant, distMaxPlant, moisDebutFleur, moisFinFleur)  
PRODUIT(codeBarre, conditionnement, nbUnites, prix, stock, #variete)  
COMMANDE(noCommande, dateCommande, modeLivraison, #pointRelais, #client)  
POINTRELAIS(id, nom, rue, codePostal, ville)  
CLIENT(noClient, nom, prenom, rue, codePostal, ville, email)  
CONTIENT(#codeBarre, #noCommande, nombre)  
PROCHE(#variete, #varieteProche)  

---

## **3. Normalisation**
Ensemble des règles pour une bonne conception (Edgar Codd, 1970) avec pour objectif d'éviter :
- Les redondances
- Les incohérences
- Les valeurs nulles

### Dépendance Fonctionnelle : 
Y dépend fonctionnellement de X si on ne peut associer qu'un Y à chaque X

***Trivial*** : X -> X ou XY -> Y 

**Ex5** 

A1 -> A4 ; A2 -> A3 ; A3 -> A2 ; A1,A2 -> A3 ; A1,A2 -> A4 ; A1,A3 -> A2 ; A1,A3 -> A4; A2,A4 -> A3 ; A3,A4 -> A2 ; A1,A2,A3 -> A4 ; A1,A2,A4 ->  ; 

### **A - 1ère Forme Normale (1FN)** 
***Tout attributs contient une valeur atomique*** : 
- Pas de valeur calculable
- Pas de structure répétitive

### **B - 2ème Forme Normale (2FN)**
- Etre 1FN
- Clé Primaire défini
- Tout autre attribut est en DF avec l'ensembe de la clé primaire

### **C - 3ème Forme Normale (3FN)**
- Etre 2FN
- Pas de dépendance fonctionnelle entre attributs non-clés
### **D - 4ème Forme Normale (4FN)**
- Etre 3FN
- Les dépendances fonctionnelles ne se font qu'entre des attributs clés et des non-clés2

# NoSQL et MongoDB

Not only SQL => not relationnal

### 1. **Modèle Hierarchique : IMS** 
Rangement des boites dans des boites avec une grande boite
### 2. **Language en réseau : Cobol en réseau**
Language Cobol d'interrogation de données : ancetre du SQL
Modèle en réseau
### 3. **Modèle Relationnel par Edgar F. Codd**
### 4. **Le Big Data**
Besoins en : 
- PétaOctets, ExaOctets
- Données hétérogènes
- Acces rapide à tout moment

Emergence de nouveaux modèles 
- 2003 : GFS
- 2004 : BigTable
- 2006 : HBase
- 2007 : Amazon Dynamo
- 2012 : DynamoDB

## **Les modèles de NoSQL**
---

### 1. **Orientés Clé-Valeur** 
AmazonS3, Redis, Riak
### 2. **Orientés Clé-Document**
Utilisation de fichier JSON, XML, ...
### 3. **Orientés Colonne**
clé et avec des colonnes 
### 4. **Orientés graphes**
DOnnées sous forme de noeuds connectés entre eux
### 5. **Orientés plain-text**
Index inversé : moteur de recherche
Des sites web associés à des termes