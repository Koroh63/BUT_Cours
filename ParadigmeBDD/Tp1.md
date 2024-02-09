# Partie 2 :

### 1.
    CREATE (n:Etudiant{NumEtudiant : 172, Nom : 'Richard', Prenom : 'Ana', Prenom2 : 'Maria'});
    CREATE (n:Etudiant{NumEtudiant : 284, Nom : 'Leroux', Prenom : 'Nicolas', Prenom2 : 'Jean'});
    CREATE (n:Etudiant{NumEtudiant : 145, Nom : 'Marc', Prenom : 'Alex'});
    CREATE (n:Etudiant{NumEtudiant : 189, Nom : 'Bern', Prenom : 'Clara'});
    CREATE (n:Etudiant{NumEtudiant : 187, Nom : 'Lavoisier', Prenom : 'Sarah'});

    CREATE(n: Cours{NumCours: 1, NomCours : 'Science des donées' });
    CREATE(n: Cours{NumCours: 2, NomCours : 'Base de données' });
    CREATE(n: Cours{NumCours: 3, NomCours : 'Virtualisation' });

    CREATE(n: Projet{NumProjet: 34, NomProjet : 'Data mining' });
    CREATE(n: Projet{NumProjet: 44, NomProjet : 'Analyse de données' });
    CREATE(n: Projet{NumProjet: 3, NomProjet : 'Machine learning' });
    CREATE(n: Projet{NumProjet: 51, NomProjet : 'Virtualisation' });

    CREATE(n: Salle{NomSalle: '301'});
    CREATE(n: Salle{NomSalle: 'Amphi'});
    CREATE(n: Salle{NomSalle: 'Lardy_108'});
    CREATE(n: Salle{NomSalle: '401'});
    CREATE(n: Salle{NomSalle: 'Lardy_110'});


### 2.

    MATCH(c:Cours),(s:Salle) WHERE c.NumCours = 1 AND s.NomSalle = "301" CREATE (c)-[r:PrendPlaceA]->(s);
    MATCH(c:Cours),(s:Salle) WHERE c.NumCours = 1 AND s.NomSalle = "Lardy_108" CREATE (c)-[r:PrendPlaceA]->(s);
    MATCH(c:Cours),(s:Salle) WHERE c.NumCours = 1 AND s.NomSalle = "401" CREATE (c)-[r:PrendPlaceA]->(s);
    MATCH(c:Cours),(s:Salle) WHERE c.NumCours = 2 AND s.NomSalle = "Amphi" CREATE (c)-[r:PrendPlaceA]->(s);

    MATCH(e:Etudiant),(c:Cours) WHERE c.NumCours = 1 AND e.NumEtudiant = 172 CREATE (e)-[r:Suit]->(c);
    MATCH(e:Etudiant),(c:Cours) WHERE c.NumCours = 1 AND e.NumEtudiant = 284 CREATE (e)-[r:Suit]->(c);
    MATCH(e:Etudiant),(c:Cours) WHERE c.NumCours = 2 AND e.NumEtudiant = 145 CREATE (e)-[r:Suit]->(c);
    MATCH(e:Etudiant),(c:Cours) WHERE c.NumCours = 1 AND e.NumEtudiant = 189 CREATE (e)-[r:Suit]->(c);
    

    MATCH(e:Etudiant),(p:Projet) WHERE p.NumProjet = 34 AND e.NumEtudiant = 172 CREATE (e)-[r:TravailleSur{Heure : "1"}]->(p);
    MATCH(e:Etudiant),(p:Projet) WHERE p.NumProjet = 44 AND e.NumEtudiant = 172 CREATE (e)-[r:TravailleSur{Heure : "2"}]->(p);

    MATCH(e:Etudiant),(p:Projet) WHERE p.NumProjet = 34 AND e.NumEtudiant = 284 CREATE (e)-[r:TravailleSur{Heure : "3"}]->(p);
    MATCH(e:Etudiant),(p:Projet) WHERE p.NumProjet = 44 AND e.NumEtudiant = 284 CREATE (e)-[r:TravailleSur{Heure : "4"}]->(p);
    MATCH(e:Etudiant),(p:Projet) WHERE p.NumProjet = 3 AND e.NumEtudiant = 284 CREATE (e)-[r:TravailleSur{Heure : "1"}]->(p);
    MATCH(e:Etudiant),(p:Projet) WHERE p.NumProjet = 51 AND e.NumEtudiant = 284 CREATE (e)-[r:TravailleSur{Heure : "1"}]->(p);
    
    MATCH(e:Etudiant),(p:Projet) WHERE p.NumProjet = 34 AND e.NumEtudiant = 145 CREATE (e)-[r:TravailleSur{Heure : "1"}]->(p);
    MATCH(e:Etudiant),(p:Projet) WHERE p.NumProjet = 44 AND e.NumEtudiant = 145 CREATE (e)-[r:TravailleSur{Heure : "2"}]->(p);
    MATCH(e:Etudiant),(p:Projet) WHERE p.NumProjet = 51 AND e.NumEtudiant = 145 CREATE (e)-[r:TravailleSur{Heure : "3"}]->(p);

### 1.

    Match (e:Etudiant) return count(e)
    Match (p:Projet) return p

### 3.
    
    CREATE (n:Etudiant{NumEtudiant : 175, Nom : 'Richard', Prenom : 'Corentin'});

### 4.

    CREATE(n: Cours{NumCours: 4, NomCours : 'NoSQL' });
    MATCH(e:Etudiant),(c:Cours) WHERE c.NumCours = 4 AND e.NumEtudiant = 175 CREATE (e)-[r:Suit]->(c);

### 5. 

    MATCH (c:Cours{NumCours: 1}),(s:Salle),(c)-[r:PrendPlaceA]->(s)  
    RETURN s.NomSalle,c.NomCours

### 6.

    MATCH (e:Etudiant{NumEtudiant: 172}),(p:Projet),(e)-[r:TravailleSur]->(p)  RETURN e.Prenom,p.NomProjet, r.Heure

### 7.

    MATCH (e:Etudiant),(p:Projet{NumProjet:51}),(e)-[r:TravailleSur]->(p)  RETURN e.Nom,p.NomProjet, r.Heure

### 8.

    MATCH (e:Etudiant),(p:Projet),(e)-[r:TravailleSur]->(p) RETURN e.Nom,p.NomProjet, r.Heure ORDER BY e.Nom

### 9.

    MATCH (e:Etudiant),(p:Projet),(e)-[r:TravailleSur]->(p) WITH e,count(r) as nb WHERE nb > 2  RETURN e.Nom,nb ORDER BY nb

### 10.

    MATCH (e1:Etudiant),(e2:Etudiant{Nom:e1.Nom}),(p:Projet),(e1)-[r1:TravailleSur]->(p),(e2)-[r2:TravailleSur]->(p) WHERE Not e2.Prenom=e1.Prenom  RETurN DISTINCT e1.Prenom,e2.Prenom,p

### 11.

    Match (e:Etudiant),(p:Projet),(e)-[r:TravailleSur]->(p) return avg(toInteger(r.Heure))

### 12.

    Match (e:Etudiant),(e2:Etudiant),(p:Projet),(c:Cours),(e)-[r1:TravailleSur]->(p),(e2)-[r2:TravailleSur]->(p),(e)-[r3:Suit]->(c),(e2)-[r4:Suit]->(c) return distinct e.Nom,e2.Nom


