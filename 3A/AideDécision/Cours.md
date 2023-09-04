# **Aide à la décision** ( Maths et IA )

Similarités basiques : k=1 un seul voisin
Similarités raisonnables : k=n plusieurs voisins 

# Algorithme des k voisins

Prise de décisions en fonctions des k voisins soit par régression ( moyenne des étiquettes des voisins ) ou par classification ( étiquette majoritiare parmi les vosins )

    Pour (xi) avec i allant de 1 à N et x* le nouvel élément :
    - 1ère étape : Calcul de la distance entre x* et tout les xi 
    - 2ème étape : Liste de couple xi et di ( la distance entre x* et xi)
    - 3ème étape : Tri de la liste par distance
    - 4ème étape : Récupartion des étiquettes sur les k premiers xi de la liste
    - 5ème étape :  - Régréssion : moyenne des étiquett (Réels)
                    - Classification : étiquette majoritaire (Discrets)

### Calcul de la distance entre **2** point A(x1,y1) et B(x2,y2) (2D): 
    d(A,B) = racine((x2-x1)²+(y2-y1)²)
### Calcul de la distance entre **2** point A(x1,y1,z1) et B(x2,y2,z2) (3D+): 
    d(A,B) = racine((x2-x1)²+(y2-y1)²+(z2-z1)²)


## Choix du k 

Par tatonnement sur un échantillion plus petit que l'ensemble, en prenant k avec le moins d'erreurs.  
Généralement k est fixé.