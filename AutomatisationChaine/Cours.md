# **Automatisation de la chaine de production**


### Développement et intégration continue

Plusieurs phases de déploiement: 

- plan
- code
- push 
- build
- inspect / test
- deploy + docs
- images 
- run



# **Partie 1** : Création des première pipeline 

utilisation du .drone.yaml pour la mise en place de différents jobs dépendant les uns des autres et utilisant des images pour fonctionner

## Objectif actuel : 

### CI : 
- build
- test
- code analyse ( sonar ) 
- docs -> déclaration de volume au build et ajout file pour utilisation par docs :  
    
    les entêtes des fonction + commentaire au-dessus pour créer le json de doc 

### CD : 
- 3 images   
- faire tourner l'image ( runner )
- faire tourner la bdd et lancer une image externe de mariadb 
- faire en sorte que les 2 se parlent avec des variables d'environement
- passer l'addresse du web service à la page web de la même facon au moment du déploiement -> dans program.cs singleton insère une dépendance , à la place de stub mettre un switch sur la variable d'environment 

## La suite : 

- rajouter les outils extérieurs pour les outils plus compliquées 
- ajouter des conditions aux drones ( drone.io conditions / starlark ) : 

        def main(ctx):
            return{
                "kind" : "pipeline",
                "name" : "CI",
                "steps": [
                    {
                        "name" : "build",

                    }
                ]
            }

changer le fichier de configuration vers .drone.star
  
Après : 
- essayer d'utiliser d'autres outils : refaire build et test sur github avec sonar sur code# [ no doc ]
- build and publish sur github 

Enfin : 
- Utilisation du release changelog builder 

- 