# Kotlin

### Evaluation
Apprentissage de Kotlin en prévision du développement en Android

#  Présentation
Language à typage statique, intégré à android studio et intellijIDEA, moins verbeux que java.Multi-paradigmes, JVM et pousse aux best-practices

Doc : https://kotlinlang.org/docs/home.html  
Playground : https://play.kotlinlang.org

Création du projet : New Porject ➜ Kotlin ➜ Créer

# Intro

- Extension des fichiers en .kt
- Si 1 instruction dans la ligne ➜ pas de **";"** en fin de ligne
- Possibilité de faire des fonctions de **premier ordre** (hors-classe)
- Déclaration et prototypes similaire à l'**UML**
- Conventions de nomage : https://kotlinlang.org/docs/coding-conventions.html

# Types

## 1. Numériques

Il n'existe pas de type Primitif, tout est donc objet même les littéraux : **2 != double &     2.0 != int**

> Possibilité de mettre des "_" dans les litéreaux sans prise en compte : 1_000_000 = 1000000

## 2. Caractères 

Les String sont **immuables/non-modiafiable** : On recréer des String pour modifier  
On accède au charactère n de la chaine str avec : 
    
    a = str[5]

- """ permet de garder le formatage 
- "| a".trimMargin permet de s'axer sur le trait 

 \+ effectue la concaténation mais préfére l'implémentation de la variable directement (string template) : 

    var str = "Bonjour $nom !"

## 3. Boolean
Basique : True ou False

## 4. Tableau
Tableau de base : 
    
    Array<Int> tab = new Array<Int>()
    tab = arrayof(1,2,3,5)
    tab.size // retourne 4

L'utilisation des types primitifs dans les tableaux permet une optimisation par Kotlin

## 5. Autre

Il n'y a pas de type "void", mais le singleton Unit. Le type Nothing existe aussi mais il représente une valeur qui n'existe pas. Il est donc impossible à instancier sauf en Exception. Ces types permettent la cohérence du sytème de type.

**.., until et downTo avec step** permettent de faire une séquence : 

    10 downto 1 step 2 // 10 8 6 4 2


# Variables

## 1. Types
- **val** : constante
- **var** : variable
    - **const** : top level (#define)

    
            const val truc = muche
            
            fun method(){
                val size = 10
                var quantity = 0;
                var++;
            }

## 2. Opérateurs

- == Compare 2 instance  
- === Compare l'adresse des instances  

De base les types ne sont pas nullables ➜ **NullPointerException**  
**Donc attetion aux oublis d'instanciation !** 

**truc?** : truc est alors **nullable** ( Attetion Truc != Truc? )
➜ Utilisation de . imossible sur les nullable : il faut utiliser ?. ou vérifier avant. On peut aussi forcer l'opération avec ***!!*** mais c'est déconseillé.

Lorsque on utilise des types JAVA nullable : Type! apparait ➜Type! est Type ou Type? 

Pour connaitre son type:    
        
    is

Cet opération est retenue pour les conditions suivantes :

    if(myst is String && myst.lenght > 0 ){ // .lenght est dispo que pour String !
        println(myst.uppercase())
    }

On peut utiliser as(unsafe) et as?(safe : évite l'exception) afin de caster un type

## 3. Comparaisons

> Le "if" reste inchangé et est comme en JAVA.

"when" est comme "switch" de JAVA mais en mieux : 

    when(x){
        0, 1 ->print("peu)
        in 2..10 -> print("moyen")
        is Strig -> print("${x.trim()} est un string")
        else -> {
            print ("rien")
            println ("block")
        }
    }
    val parité = if(x.isOdd()) "impair" else "pair"

    println(
        when{
            x.isOdd() -> "impair"
            x.isEven() -> "pair"
            else -> "bizarre"
        }
        )

## 4. Boucles
>"continue" "while" et "break" restent inchagés et sont comme en JAVA

"for" retourne maintenant un iterator sur les classes possèdant hasNext() et Next()  
"break" lui peut désormaais cibler la boucles à casser.

## 5. Exceptions

Identique au JAVA avec le "check Exception" en moins.

# Fonctions 
possibilité de top-level ( hors-classe)

    fun sum(a: Int, b: Int): Int {
        return a + b
    }

si une seul instruction : 

    fun sum(a: Int, b: Int ) : Int = a+b

ou

    fun sum(a: Int, b: Int ) = a+b

param avec val par défauts
param nommés 

    fun Box.setMargins(left : Int, right : Int)
    myBox.setMargins(left = 10)

vararg : nombre de paramètres variable 

    fun foo(vararg strings: String){...}
    foo ("bar")
    foo ("bar","baz")

spread operator * 

fonction dans fonctinos 

Fonctions : éléments de premier rang => elles ont un type (param, type retour)

    (A,B) -> C

fonction qui prend du A et du B et qui renvoi du C

    () -> Unit 

prend rien et renvoi rien 

    A.(B) -> C
fonction sur A qui prend B et renvoi C

.map pour appliquer un truc à une liste 
.foreach parcours 


Fonctions d'extensions permet d'étendre des classes en dehors de celles String.reverse(Str) : Str

Android donne pleins d'extensions pour écrire plus facilement du Kotlin pour android

Fonctions infix : comme des opérateurs 

    String.open(rights: Acces) file
    File f = "/home/koroh/test.txt" open Acces.read /return le type file en lecture

Doc

Dokka 
comme le javadoc

