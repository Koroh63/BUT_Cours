# TP2

1) Traduire le MCD du TP1 en MLD :

- Categorie(no/,nom)
- Reglement(no/,date,montant,#noFacture)
- Facture(no/,date,#client)
- Type(type/)
- Client(no/,nom,prenom,rue,CP,ville,#type)
- Materiel(ref/,designation,marque,caution,tarifJour,pénalitéJour,#categorie)
- Unite(no/,usure,#ref)
- Taxer(#type/,#categorie/,taux)
- Louer(#noClient/,#noUnite/,debut/,finPrevue,finEffective)