# Qualité de développement
## *Les test*

Rapport d'équilibre entre le coup du bug et le coup du test : plus le bug est dangereux/couteux plus on effectuera de tests
-> Tester c'est assumer les bugs

Test => jeux d'essais => couverture proche mais jamais 100% ( on ne peut pas tout tester )

Les test ne sont que le resultat de l'automatisation des essais

> CI (intégration continue) : de base c'est le push mais on fragilise l'existant donc on doit vérifier donc on doit faire des tests.  
-> Intégrer de nouvelles briques en vérifiant que ca reste fonctionnel.

### **Les différents types de test:** 

- ***Test Fonctionnel :*** vérification des cas d'utilisation (fonctionnalités) 
- ***Test Unitaire :*** tester une unité (classe, groupe de méthode, etc ...), plus particulièrement les méthodes -> 1 classe = 1 fichier de test

