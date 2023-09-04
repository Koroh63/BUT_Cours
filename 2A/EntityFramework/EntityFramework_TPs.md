# Entity Framework

## 1. Création du projet 

New Solution ➜ AppConsole ➜ Installation des NuGets

## 2. Premières Classes

### **MyDbContext :**

    class MyDbContext extends DBContext{

        public DBSet<ArtistEntity> artists {get; set;}

        override OnConfiguring(){
            base.laguir(optionBuilder);
            optionBuilder.UseSQLite('$Data Source=True' EFA="test.db);
        }
    }

### **ArtistEntity :**

    class ArtistEntity{
        public Int Id{get; set;}
        public String Prenom{get; set;}
        public String Nom{get; set;}
        public Date DateNaissance{get; set;}
    }

### **Program.cs :**

    using(var context = new ArtistsDbContext()){
        context.Artists.AddRange(new ArtistEntity(
        {
            "Morgan","Lee",17-05-2001)
        }
        )
    } //dispose
    context.SaveChanges(); // pour enregistrer

## 3. Lancement 

Modifier CsProj pour ajouter Start working directory (exemple 041 004) sinon une exception "UpdateException" sera levée

En console 

    # dotnet ef migrations add "myMigration" //build et créer les migrations
    # dotnet ef database update //créer la base 

> Supprimer les migrations(dossier) tant qu'on n'as pas une version fonctionnelle

On peut utiliser Fluent API ( on écrit dans dbcontext) pour éviter les annotations -> Dans la fonction OnModelCreating

## 4. Utilisation

> Double click sur la base de données .sqlite permet d'accéder à celle-ci si on a un browser pour sqlite.

Uitilisation de Link to entities : 

    using(var context = new ArtistsDbContext()){
        context.Artists.Where(a=>a.BirthDate>new DateTime(2002,12,12)).OrderByDescending(a=>a.lastname);
        foreach(var a in artists){
            Console.WriteLine($"{a.FirstName} {a.LastName} ({a}))
        }
    } //dispose
    context.SaveChanges(); // pour enregistrer
> On peut modifier la requête si elle n'est pas assez optimisé
## 5. Propreté / Séparation de la bibliothèque de classe 

- MyEFLib : stock le DBCOntext et ses Entitys 
- Project :  
- App cosole : consomme la biblio de classe 

On se place dans le bdProject ou dans le startupProject

## 6. Propreté 

Pour faire bien : 

DBContext + entity 
StubContext
TrucEF : classes

On ajoute un namespace Model : 
- Couche abstraite : interface IDataManager{
    getnbArtists
    getArtists
    GetArtists by id
    add 
    etc... CRUD
}

Shema : 

ajout de biblio de classe avec Dbdata manager qui implémente Idatamanager  dépend de model et my efLib

public DbDataMANGER ( artis context ){
    this context = context
}
: private readonly artistsDbCOntext context{ get set}