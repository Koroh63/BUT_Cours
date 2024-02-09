# Complexité d'un problème algorithmique 

## Problème du tri 

Borne inférieure à o(n) -> lire tout les éléments de la liste   
Mais a-t-on mieux que le tri fusion O(n log(n))

Utilisation d'un arbre de décision pour un tri sur n éléments mais il est de hauteur nlog(n)

tri en temps linéaire qui ne sont pas par comparaisons :
- Tri par dénombrement : les nombres sont bornées O(n)
- tri par bases : nombre de longueur max fixés ( tri des unités, puis dizaines, puis ...) O(n)

## Problème de décision :

### K-colorabilité : 

tester tout les colorations k^n -> au pire des cas 

- 2 colorable : 1 point avec une couleur puis les voisins d'une autres puis les voisins des voisins de la 1ere etc ...
- k colorable : algorithme exponentiel

### SAT :

formule propositionnelle F en CNF 

Problème : F est-elle satisfaisable ?