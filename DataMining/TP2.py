import numpy.random as random
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import streamlit as sl
import sklearn.preprocessing as pre

sl.title("TP2")
tab1, tab2, tab3, tab4 = sl.tabs(["Normalisation des données", "Exercice B", "Téléchargement et importation de données","Génération de données et affichage"])


# exo A 
matrice = np.array([[1, -1, 2], [2, 0, 0], [0, 1, -1]])
matriceNormed = pre.scale(matrice)
X2 = pre.MinMaxScaler().fit_transform(matrice)

with tab1:
    choice = sl.selectbox("Select what matrix to work on :",("Default","Normalisation","MinMax Normalisation"))
    if(choice=="Default"):
        m = matrice
    else:
        if(choice=="Normalisation"):
            m = matriceNormed
        else:
            m = X2
    sl.write(m)
    sl.write("Moyenne : " + str(np.mean(m)))
    sl.write("Variance: "+str(np.var(m)))

# exo B 

from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784')
x = mnist.data
y = mnist.target

with tab3:
    sl.write("Matrice des données MNIST :")
    sl.write(x[:3000])
    
    sl.write("Nombre de données :", x.shape[0])
    sl.write("Nombre de variables :", x.shape[1])
    
    sl.write("Numéros de classes pour chaque donnée :", np.unique(y))
    
    sl.write("Moyenne par variable :")
    sl.write(np.mean(x, axis=0))
    
    sl.write("Écart type par variable :")
    sl.write(np.std(x, axis=0))
    
    sl.write("Valeurs min par variable :")
    sl.write(np.min(x, axis=0))
    
    sl.write("Valeurs max par variable :")
    sl.write(np.max(x, axis=0))
    
    sl.write("Nombre de classes :", len(np.unique(y)))


# exo D 

from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=1000, n_features=2, centers=4, random_state=42)

fig1, ax1 = plt.subplots(figsize=(8, 6))

# Tracer les points de données avec des couleurs correspondant aux classes
scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')

# Définir les limites des axes x et y
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)

# Ajouter un titre à la figure
ax.set_title('Données générées avec make_blobs')

# Ajouter des titres aux axes x et y
ax.set_xlabel('Variable 1')
ax.set_ylabel('Variable 2')

# Afficher la légende
legend = ax.legend(*scatter.legend_elements(), title="Classes")
ax.add_artist(legend)


# Q4 

np.random.seed(42)
X1, y1 = np.random.multivariate_normal(mean=[0, 0], cov=[[1, 0.5], [0.5, 1]], size=100), np.zeros(100)
X2, y2 = np.random.multivariate_normal(mean=[3, 3], cov=[[1, 0], [0, 1]], size=500), np.ones(500)

X = np.vstack((X1, X2))
y = np.hstack((y1, y2))

fig, ax = plt.subplots(figsize=(8, 6))


scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')

# Ajouter un titre à la figure
ax.set_title('Données générées')

# Ajouter des titres aux axes x et y
ax.set_xlabel('Variable 1')
ax.set_ylabel('Variable 2')

# Afficher la légende
legend = ax.legend(*scatter.legend_elements(), title="Classes")
ax.add_artist(legend)

# Afficher la figure dans Streamlit
st.pyplot(fig) 

with tab4:
    sl.pyplot(fig)



