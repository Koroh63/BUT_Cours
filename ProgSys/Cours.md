# Programmation système 

- Sémaphores ( IPC )
- Segments de mémoire partagée

## Les Threads : 

### Ordonnancement des processus

Contrôlé par sched.h mais peut être utilisé manuellement.

3 types : 
- FIFO -> temps réel 
- Round Robin -> temps réels
- Sched_Other : temps préemptif 

Commutations ( prendre et rendre le proc ) implicites ou explicites

### Définition : 

Thread : executé DANS un processus
- Donne plusieurs activités au processus 
- Plus efficace que plusieurs processus 
- Infos propres à chaques thread ( pile & contexte ) & infos partagées ( segments de données créés au départ ) 
- Partage dépendant de l'implémentation
- Espace d'addressage commun 

### Fonctions et Types : 

Erreurs : Pas de errno -> Si 0 ok 

Compilation avec -D_REENTRANT

pour connaitre le num de thread au sein du prog : pthread_self 



