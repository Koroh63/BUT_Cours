# Qualité de Dev 

perso.limos/sebastien.salva

Tests : phase de validation de l'implémentation 

boite blanche : système dont la structure est entièrement accessible 
boite noire : structure interne inconnue, seules les interfaces sint connues (PCO = Point de contrôle d'observation )
boite grise : accès partiellement au système : bdd connue, code inconnu 

Test classique : 

spécification -> création -> run : difficultées au niveau des spec 

Tests écrits à la main ou généré 

Verdicts du test : 
- PASS
- FAIL
- INCONCLUSIVE 

Types : 

- Caractéristique 
- Granularité ( unités, intégration, système, acceptation du client, non-régression)
- Accessibilité
- Usager 
- Interopérabilité
- Robustesse : stresser le système dans un cadre inattendu avec des aléas (outils)
- Conformité : Test générés depuis la spécification ( unitaires, non-régression, fonctionnel), test basé modèle ( )

Cout d'une vraie phase de test : au moins 40% 

unitaire trop chiant su API rest 

test de conformité de l'application : intégration et fonctionnel après unitaire ( top-down du spec ou bottom-up du code)
    - Sécurité ( entrées, logs[ trop verbeux ], pénétration, crack de mdp)

JUnit 