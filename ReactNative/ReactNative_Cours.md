# ReactNative : Cours


### Evaluation :

*20h de TP*   

#### Doc (4pts) :  

- **Sketchs**

#### Basics (10pts) : 

- **Navigation (2pts)** : Tab bottom navigation + 1 button  
- **Store (2pts)** : Read data from redux store 
- **Actions (1pts)** : Update data to redux store  
- **Display list of items (2pts)** : FlatList, VirtualizedList or SectionList 
- **Display image (1pts)**
- **Child props (1pts)**
- **TextInput (1pts)**

#### Application Features (6pts) :  

- Use **web api (2pts)** 
- **Store** favorite data **(2pts)**  
- Write **tests (2pts)** 

#### Bonus (only if basics mastered) :  

- Dark/Light mode **switch (2pts)**  
- Sexy **UI (2pts)**  




# Basics ReactNative 
*Qu'est ce que ReactNative ?* : C'est similaire à JavaScript mais pour mobiles : surcouche au-dessus du native , la partie vue est seule à être compilée et javascript et modules natifs ne sont qu’éxécutés  

## 1. **Ui component**
 
- Buttons, Switch  
- Section List, Flat List 
- View, ScrollView
- TextImage, Text Input 
- StyleSheet 

## 2. **Stylesheet** 

## 3. **Flexbox css** 

- Flex-direction 
- flex wrap 
- justify-content 
- align-items 
- align-content 

## 4. **JSX** 

## 5. **Props** 

Les fichiers prennent forment en 3 parties :  

- Props : défini les données et les passes aux components 

- Component : passé au mobile pour l’affichage , avant le return : liberté de faire ce qu’on veut  

- Stylesheet : avec une seule méthode :        

        void .create(){  
            définition des styles à la CSS  
        }     

# State Management (Redux) 

Etat partagé par les composants et écrans dans le store, il ne sera pas sauvegardé, 
On utilise donc redux dans react, qui permet d'utiliser le store, il n'y en as qu'un par application

# Navigation 

## TPs : 

Arbo: 
- assets 
- components
    - props : type
    - fonction render : notre composant
    - feuille de style : 
- navigation
    - navigation.tsx
- screens
    - HomeScreen.tsx
- App.tsx : main point d'entré
- app.json : Android ou ios, icon, version
- package.json : nugets , dependances


### les écrans : 

pas de propriétés: on peut utiliser nos composants 

### FlatList : 
3 propriété principales :

- data 
- renderItem
- keyExtractor : avoir un identifiant unique pour chaque item => il faut qu'on lui donne la clé unique de l'item pour chaques 

    export const NOUNOURSLIST

    <Flat>

### nAVIGATION AVEC bottom tab bar

faire imort , créer bottome tab bar , 
toute naivgation doit se faire dans le navigation container 

# Native features 
