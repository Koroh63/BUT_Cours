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

#### *Exemple :*
""MLD""

---

## **3. Normalisation**
Ensemble des règles pour une bonne conception (Edgar Codd, 1970) avec pour objectif d'éviter :
- Les redondances
- Les incohérences
- Les valeurs nulles

### Dépendance Fonctionnelle : 
Y dépend fonctionnellement de X si on ne peut associer qu'un Y à chaque X

### **A - 1ère Forme Normale (1FN)** 
***Tout attributs contient une valeur atomique*** : 
- Pas de valeur calculable
- Pas de structure répétitive

### **B - 2ème Forme Normale (2FN)**
- Etre 1FN
- Clé Primaire défini
- Tout autre attribut est en DF avec l'ensembe de la clé primaire

## NoSQL et MongoDB
