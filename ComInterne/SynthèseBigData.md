# Synthèse DataFramework

## Intro

Ajouter présentation mapReduce 
### Contexte
Avec une augmentaion exponentielle de la quantité des données générées, nous sommes venus à parler de Big Data représentant les système contenant d'immenses quantité de données : celui-ci est défini par les 4 V : 
- Volume
- Variété
- Véracité
- Velocité

***Problématique :*** *Comment concevoir des environements evolutifs ? Comment tolérer les fautes et concevoir des solutions efficaces ?*

Cependant une présentation de MapReduce est nécessaire en premier: 
Le modèle de programmation MapReduce a été développé par Google en 2004 pour gérer le traitement parallèle de grands ensembles de données en masquant les détails de la parallélisation, du stockage distribué, de l'équilibrage de charge et de la tolérance aux pannes. Ce modèle repose sur deux fonctions clés : Map et Reduce, qui transforment des paires clé-valeur en paires clé-valeur intermédiaires, qui sont ensuite regroupées et traitées par Reduce. Cependant, bien que MapReduce soit efficace, il présente des défis liés à la gestion des données et à la planification. La gestion des données implique la sélection d'une structure de données et d'un flux de travail appropriés, tandis que la planification implique des décisions de planification complexes basées sur des informations telles que la disponibilité des ressources et la localisation des données pour minimiser les coûts de communication et résoudre les problèmes de charge inégale.

Donc pour le plan, dans un premier temps nous étudions les les cadres de travail du Big Data pour ensuite évaluer et comparer leurs performances pour enfin présenter les meilleurs pratiques lors de leur utilisation.




## 1er Paragraphe
Com MapReduce:
Com MapReduce est une extension de MapReduce qui permet la communication entre les fonctions Map pendant l'exécution d'un travail MapReduce. Ce système utilise un coordinateur entre les fonctions Map qui utilisent un espace partagé pour permettre la communication. Cette capacité de communication permet un partage efficace des données entre les fonctions Map et est particulièrement utile dans les applications d'apprentissage automatique et de traitement de graphes.

Twister:
Twister est une extension de MapReduce conçue pour gérer les problèmes MapReduce itératifs. Twister offre plusieurs fonctionnalités pour prendre en charge les calculs MapReduce itératifs, notamment la distinction entre les données statiques et variables, l'accès aux données via des disques locaux et les tâches MapReduce pouvant être mises en cache. Ce système est particulièrement utile pour les applications telles que l'apprentissage automatique et le traitement de graphes qui nécessitent plusieurs itérations.

HaLoop:
HaLoop est une version modifiée de Hadoop MapReduce conçue pour les applications MapReduce itératives. HaLoop améliore l'efficacité des applications itératives en rendant le planificateur de tâches conscient de la boucle et en ajoutant divers mécanismes de mise en cache. HaLoop offre une interface de programmation pour exprimer des tâches d'analyse de données itératives et est particulièrement utile dans les applications telles que l'apprentissage automatique et le traitement de graphes.

DATAMPI:
DATAMPI est une extension de MPI qui prend en charge la computation de type MapReduce. DATAMPI abstrait les modèles de communication clé-valeur dans un modèle de communication bipartite, qui présente quatre distinctions par rapport à MPI: les fonctionnalités dichotomiques, dynamiques, centrées sur les données et diversifiées. DATAMPI vise à utiliser des techniques de communication MPI optimisées sur différents réseaux, tels que InfiniBand et 1/10GigE, pour prendre en charge les travaux MapReduce.

Hadoop:
Hadoop est un projet open-source qui se compose de deux composants principaux: Hadoop Distributed File System (HDFS) pour le stockage de données et Hadoop MapReduce, une implémentation du modèle de programmation MapReduce. HDFS fournit un système de fichiers distribué et évolutif pour stocker des fichiers volumineux sur des machines distribuées de manière fiable et efficace. Hadoop MapReduce est un modèle de programmation conçu pour traiter de grands ensembles de données dans un environnement informatique distribué. Hadoop est largement utilisé dans diverses applications telles que le traitement de journaux, les systèmes de recommandation et la détection de fraudes.

Spark:
Spark est un framework Big Data populaire utilisé par de nombreuses entreprises telles que Yahoo, Baidu et Tencent. Un concept clé de Spark est Resilient Distributed Datasets (RDD), qui sont des collections immuables d'objets répartis sur un cluster Spark. Spark offre plusieurs APIs, dont Spark Core, Spark Streaming, Spark SQL, Spark MLLib et GraphX. Spark Core est le moteur d'exécution général sous-jacent pour la plateforme Spark, 
## 2e Paragraphe


## Conclusion
### Retour Final 
### Elements essentiels
### Ouverture

