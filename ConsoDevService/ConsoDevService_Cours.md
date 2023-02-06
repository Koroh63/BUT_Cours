# Consommation et Développement de services : Cours 

### Evaluation

Projet commun avec Marc Cheval
"Grille notation"

#### 1. **API** 24pts
#### 1. **Documentation** 16pts
#### 1. **Bonus**

# API
**Qu'est ce qu'une API :** Application Programming Interface, Exploiter des ressources distantes 
> URI : Uniform Ressource Identifier (url + urn)  
> Protocol Http : utilisé pour effectuer les requêtes à l'API

Nous utilisons un API type Rest (Representationnal State Transfer) avec les conventions qui vont avec : 
- **Stateless** : Pas de session : utilisation de Tokens
- **Layered** : Permettre l'ajout d'intermédiaires (surcouche)
- **Verbes** : actions sur les ressources 
    - Get : Récupération
        - By Id doit retourner un élément de manière unique
    - Post : Création 
        - Récupération du DTO et conversion en entité
        - Ajout et recup du ajouté 
        - Retour du resultat reconverti en DTO ( nameofgetbyid), new{Id =1}, championResultDTo)
        - ne pas tester le code de retour mais le contenu de celui-ci, et si le cast n'est pas null  
    - Put : Mise à jour
    - Delete : Suppresion

Utilisation des codes de retours Internet : 
- **100** : informations
- **200** : succès
- **300** : retours
- **400** : erreurs coté client
- **500** : erreurs serveurs 

*Richardson Matury Model* :  Définition des niveaux de qualité des API ( définit la note sur les TPs [ Niveau 2 et - à savoir ]) :
- **Niveau 0** : RPC HTTP
- **Niveau 1** : segmentation en ressource
- **Niveau 2** : utilisation des verbes et des codes de retours : Savoir
- **Niveau 3** : utilisation des controles hypermedia 
: my EFLIB : biblio de classes
## Pour les Tps : 
- Rider de JetBrains ou Visual Studio (.net 6)

1. Créer le projet
2. Selectionnier *API Web ASP.net core (C#)
3. Activer https, docker, controllers et openAPI
builder .Services.ADDScoped(IDAtaManager, StubData()) <-
builder .Services.ADDTransient(IDAtaManager, StubData)
builder .Services.ADDSingleteon(IDAtaManager, StubData)

IDATAManager datam.ianager


> **DTO** : Data Transfer Object, permet de transformer une classe afin d'en faire l'envoi, notamment si l'on ne veut pas stocker tout dans la base de données. 

***A avoir fait***

***Déploiement***

Conteneur avec API puis peut etre avec BDD