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
        context.Artists.Add(new ArtistEntity("Morgan","Lee",17-05-2001))
    } //dispose

## 3. Lancement 

Modifier CsProj pour ajouter Start working directory (exemple 041 004) sinon une exception "UpdateException" sera levée

En console 

    # dotnet ef migrations add "myMigration"
    # dotnet ef database update

> Supprimer les migrations(dossier) tant qu'on n'as pas une version fonctionnelle
