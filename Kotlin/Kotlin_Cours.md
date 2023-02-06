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
- Android donne pleins d'extensions pour écrire plus facilement du Kotlin pour android

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

## **1. Types**
- **val** : constante
- **var** : variable
    - **const** : top level (#define)

    
            const val truc = muche
            
            fun method(){
                val size = 10
                var quantity = 0;
                var++;
            }

## 2. **Opérateurs**

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

## 3. **Comparaisons**

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

## **4. Boucles**
>"continue" "while" et "break" restent inchagés et sont comme en JAVA

"for" retourne maintenant un iterator sur les classes possèdant hasNext() et Next()  
"break" lui peut désormaais cibler la boucles à casser.

## **5. Exceptions**

Identique au JAVA avec le "check Exception" en moins.

# Fonctions 
Les fonctions sont des élèments de premier rang, on peux donc mettre des fonctions dans des fonctions et celle-ci ont toutes un type.

Possibilité de faire des fonctions top-level ( hors-classe )

    fun sum(a: Int, b: Int): Int {
        return a + b
    }

Une fonction de contenant qu'une seule instruction : 

    fun sum(a: Int, b: Int ) : Int = a+b

ou

    fun sum(a: Int, b: Int ) = a+b
  

On peut aussi définir les fonctions avec des valeurs par défault pour les paramètres et nommer les paramètres :

    fun Box.setMargins(left : Int, right : Int)
    myBox.setMargins(left = 10)

Ou aussi avoir un nombre de paramètre variable avec vararg : *param permet de lui faire passer des Array (spread operator)

    fun foo(vararg strings: String){...}
    foo ("bar")
    foo ("bar","baz")

 


Une fonction qui prend du A et du B et qui renvoi du C :

    (A,B) -> C

Une fonction qui ne prend rien et ne renvoie rien : 

    () -> Unit 

Une fonction sur A qui prend du B et renvoie C :

    A.(B) -> C

Il est possible d'effectuer des fonctions d'extensions de classes existantes en dehors de celles-ci: 

    String.reverse(Str) : Str

Les Fonctions infix permettent d'appeler les fonctions comme des opérateurs :

    String.open(rights: Acces) file                     //ouvre le file de facon classique
    File f = "/home/koroh/test.txt" open Acces.read     //return le type file en lecture avec infix



# Listes
.map pour appliquer un truc à une liste 
.foreach parcours 

# Doc

On utilise Dokka qui est comme javadoc mais en mieux 

# Classe et Objets

Définisseurs de visibilité
- public : par défault
- private
- internal
- protected

Il existe une différentiation entre le constructeur principal( au moment de la définition de la classe) 

    class Person(name: String){
        private val nameUpper = name.uppercase()
        init{
            println("My name is : $nameUpper.")
        }
    }

et les constructeurs secondaires : 

    constructor(name: String,age: Int): this(nale){
        this.age=age
    }

> L'utilisation uniquement du principale avec des paramètres par défault est plus "Kotlin Spirit"

Afin d'ajouter des visibilités sur les constructeur il faut mettre le mot clé constructor après la visibilités

le mot clé var/val permet de déclarés les paramètres du constructeurs comme attributs (val= getter et var = getter/setter)

    class Person{
        var name = "John";
    }
    john = Person();
    john.name

Cependant une syntaxe compélte est disponible 

    var speed: Int
        get() = field*100;
        set(value){
            if(value>=0){field=value}
        }

Classe de données : 

data class Person(var name:String, var age: Int)

- Pas possbile de les mettre en abstract, open, sealed ou inner
- Le Ctor principal a au moins un paramètre.
- Les paramètres des Ctor doivent tous être marqués val ou var
- equals,hashcode toString générée auto
- La méthode Copy permet de copier l'objet en changeant certains paramètres => Pattern Prototype
- La méthode component déstructure la classe :

    val (name,age) = john 
    println($name) // affiche john

# 2. Héritage 

Toutes classes hérites de Any != java.lang.Object
- open
Il faut ouvrir les classes à l'héritage 
On précise si la classe est ouverte à l'héritage : 

    open class Base(arg: String)
    class Derived(num:Int):Base(num.toString())

Pour les ctor secondiares il faut ultimement appelé le ctor principale de la mère avec super 
On redefini les méthode avec override si elle son open 
si override -> open 
mais si on veut stopper on marque final

pour les prorpiété peuvent être redefini de val en var aussi

- abstract : pas instantiable forcément open , propriétés abstraites :

        abstract class Base{
            abstract val arg: String
        }

        class Derived : Base{
            override val arg: String
            get()="Something"
        }
    
- sealed : classe abstraite avec ctor privée qui permet d'^tre redérivé dans les limites des classes défini ici : permet d'étudier le pattern et de comparer le type, permet d'avoir une hiérarchie 

        when(type){
            is Caduque -> dosmth
            is Persistant -> DOSMTH
        }
- inner : permet de définir des classes dans d'autres pour appuyer l'encapsulation

        class Outer{
            private val bar:Int= 1
            class Nested {
                fun foo() = bar
            }
        }
        val demo = Outer().Inner().foo() // demo = 2

# 3. Interfaces

Entités abstraites ne contenant pas d'état mais possibilité de définir des implémentations par défault des méthodes( sans faire appel à des attributs ) mais les propriétés peuvent être mises -> val avec getter implémenter 

    interface Named{
        val name:String
    }

    interface FullNamed: Named{
        val firstName: String
        val lastName: String
        override val name: String get()= "$firstName $lastName"
    }
    class Person(
        override val firstName: String
        override val lastName: String
    ): FullNamed

mots clé object : défini un singleton
companion object

4. Surcharche d'opérateurs 
défini des opérateurs sur les nouveaux types

    