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
- Granularité ( Isolation : unitaire, intégration,fonctionnel, système, non-régression)
- Accessibilité
- Charge / Performances 
- Interopérabilité
- Robustesse : stresser le système dans un cadre inattendu avec des aléas (outils)
- Conformité : Test générés depuis la spécification ( unitaires, non-régression, fonctionnel), test basé modèle ( )
- Sécurité 

Cout d'une vraie phase de test : au moins 40% 

unitaire trop chiant su API rest 

test de conformité de l'application : intégration et fonctionnel après unitaire ( top-down du spec ou bottom-up du code)
    - Sécurité ( entrées, logs[ trop verbeux ], pénétration, crack de mdp)

## JUNIT

Pour appeler des fixtures :
    @BeforeAll 
    @BeforeEach
    @AfterAll
    @AfterEach

Pour paramétrer les tests :
    @Test
    @Disabled (si un test à ça il sera pas lancé)
    @Order(nombre) pour ordonner tes tests

t'as aussi de l'assertion par contrat qui te permet entre autre de rendre les messages plus verbeux ce qui peut aider à debugger 

ça te permet aussi de faire des suppositions pour remplir des conditions
genre supposer qu'un fichier existe pour pas que ça te mette d'erreur par rapport à ça 

PHPUnit fonctionne de manière assez similaire à Junit
mais il faut faire attention à ce que ta version de PHP Unit soit la même que ta version de PHP

PHPUnit a aussi des fixtures 
il propose aussi de faire des suites de test où grossièrement tu vas enchaîner plusieurs tests

On a aussi vu le fait de tester en isolation : c'est de simuler des composants dont on dépend 
Comme par exemple la classe mère d'une classe que tu test

pour ça tu as sois le stub sois le mock
dans le stub tu simule une classe / composant et c'est tout -> tu lis les données 
dans le mock tu simule aussi la classe / composant mais tu va aussi faire des tests dessus -> tu vérifie l'état modifié à la fin

et après il nous a parlé vite fait de deux trois outils de test

Given when then : structuration des test qui permet de faire un lien avec les User Story
Précondition condition action

Normes ISO : Qualité Logicielle 
CMMI : Capability Maturity Model Integration ( Evalue les process d'une entreprise et la gestion de projet informatique notamment), marche sur 5 niveau :
- Initial : Rien, aucune gestion 
- Discipliné : 
- Ajusté : Monitoring de projet, gestion des risques et prévision des projets 
- Gérer quantitativement : Nombreux indicateurs, et planifications avec des process
- En Optimisation : permet de tout anticiper/gérer  

TMMI : 
- Initial : Idem 
- Managé : Stratégie, monitoring et environement 
- Defined : Gestion d'organisation des test, entrainement : non-fonctionnel
- Measured : 
- Optimisation : 


Question : 

@Test
function

