# NBA Player Tracker

__Membres de l'équipe__ : `Bourquenoud Nathan`, `Hirschi Laurent` et `Pasquier Benjamin`

## 1. Introduction

La National Basketball Association a été créée en 1946, sous le nom de Basketball Association of America avant d'être renommée en 1949. Jusqu'à aujourd'hui, cette ligue a évolué dans de nombreux aspects, les attentes des entraîneurs ou des directeurs sportifs ont donc également changé. Par exemple, l'arrivée de la ligne à trois points dans les années 80 a changé le jeu à jamais, au point que l'habilité des joueurs aux tirs à trois points demeure aujourd'hui une des compétences les plus recherchées. Les salaires ont également augmenté drastiquement et il est aujourd'hui difficile de juger si un joueur est payé de manière adéquate par rapport à ses performances. Ce projet a donc pour but de visualiser les caractéristiques des joueurs NBA selon différents angles afin d'envisager des achats, des ventes ou des transferts qui permettraient d'améliorer l'équipe de l'entraîneur ou du directeur sportif.

## 2. Choix des données

La NBA enregistre un très grand nombre de statistiques durant les matchs disputés mais également toutes sortes d'informations concernant les joueurs et les équipes. Ces données se trouvent sur le [site web officiel](https://www.nba.com/) de la NBA et peuvent être accessibles via des APIs. Étant donné qu'il existe des sources de données plus simples à manipuler, cette API n'est pas directement utilisée. Dans le cadre de ce projet, les données sources de données suivantes sont utilisées :
* L'[API Python](https://github.com/swar/nba_api) proposé sur Github par l'utilisateur [swar](https://github.com/swar), permettant d'accéder facilement aux APIs du site officiel de la NBA et donc de toutes les données qu'il contient.
* Les données salariales du site [basketball-reference.com](https://www.basketball-reference.com/contracts/players.html) qui contient les salaires de tous les joueurs actuels de la NBA.

L'évolution du salaire des joueurs étaient également prévu comme visualisation mais nous n'avons pas trouvé de source de données contenant les salaires des joueurs durant les années précédentes (sans avoir à les récupérer avec du web scraping). Nous avons donc décidé d'uniquement inclure les salaires actuels des joueurs.

### 2.1 Constitution des données finales

Les données récupérées sont traitées et structurées afin d'être utilisées facilement par l'application web. Elles sont stockées dans des fichiers au format JSON ou CSV. La base de données constitées contient des informations de 128 joueurs actuels de la NBA, qui ont été choisies en fonction de leurs performances au cours de la saison actuelle (2021-2022). Bien entendu, nous aurions pu inclure tous les joueurs actuels de la NBA, mais dans le cadre de ce projet, nous avons décidé de limiter la taille de notre base de données afin de pouvoir travailler plus facilement avec les données. Plus précisément, les données de ces joueurs sont donc les suivantes :
- __Les informations statiques à chaque joueur__ (nom, prénom, date de naissance, taille, poids, poste, équipe actuelle, salaire actuel, etc.). Un score de performance a été calculé pour chaque joueur qui se base sur ses statistiques durant la saison actuelle. Ce score est calculé en prenant compte le nombre de points, d'assistances, de rebonds, de contres, d'interceptions, de balles perdues et de l'habilité aux tirs. Ce score est ensuite normalisé afin de pouvoir comparer les joueurs entre eux.
- __Les stastiques des joueurs pour chaque saison__ (points par match, rebonds par match, assistances par match, habilité aux tirs, etc.).
- __La localisation des tirs pour chaque joueur et chaque saison__. Pour chaque joueur, le nombre de tirs marqués et effectués à chaque localisation du terrain (51*48 localisation) est enregistré, par saison.

## 3. Technologies utilisées

Ce projet est réalisé sous la forme d'application web, avec une partie frontend pour la visualisation de l'information et une partie backend pour la gestion des données. Les technologies utilisées sont les suivantes :

* __[Python](https://www.python.org/)__ : language de programmation utilisé pour le traitement des données et la création d'une interface entre le frontend et les fichiers de données. Il est logiquement également utilisé pour la création de l'application web avec Dash Plotly.
* __[Dash](https://plotly.com/dash/)__ : librairie Python qui permet de créer rapidement des applications web interactives de visualisation et d'analyse de données à l'aide de code Python. Il est construit sur la bibliothèque Plotly.js et utilise le framework Flask pour servir les pages web et exécuter le code Python.
* __Autres libraries Python__ : principalement [Pandas](https://pandas.pydata.org/) pour le traitement des données, [Numpy](https://numpy.org/) pour le calcul scientifique et [Jupyter Notebook](https://jupyter.org/) pour la création de notebooks pour le traitement des données.

## 4. Intention et public cible

L'objectif de ce projet est de permettre à des entraîneurs et/ou des directeurs sportifs d'équipe de la NBA de chercher et trouver des joueurs évoluant dans la ligue qui correspondent au mieux à leurs attentes. La réalisation de ce projet leur permet de naviguer parmi tous les joueurs de la ligue et de les comparer selon plusieurs critères (statistique particulière, salaire, performance globale, localisation des tirs du joueur) afin de trouver la(les) pièce(s) manquante(s) de leur équipe. 

L'application développée sert donc de tableau de bord composé de plusieurs visualisations de données permettant à des entraîneurs et directeurs sportifs de la NBA de trouver efficacement les joueurs qui correspondent le mieux à leurs attentes.

## 5. Choix des représentations

Notre application interactive est un tableau de bord composé de différentes représentations. Elle est composée de deux parties principales :
- Une partie supérieure contenant une représentation globale des données dans un tableau,
- Une partie inférieure contenant plusieurs représentation plus détaillées des données.

### 5.1 Vue globale

La partie supérieure de l'application contient une représentation globale des données dans un tableau. Elle offre un premier aperçu des informations et des statistiques des joueurs qui peuvent être représentées textuellement. Ce tableau est représenté par l'image ci-dessous.

<img src="./readme_resources/test.jpg" alt="drawing" width="300" style="display: block; margin: 0 auto"/>

Toutes les données de ce tableau sont statiques, les premières colonnes contiennent les informations générales des joueurs (nom, prénom, date de naissance, taille, poids, poste, équipe actuelle, salaire actuel, etc.) et les colonnes suivantes contiennent les statistiques des joueurs durant la dernière saison. Le tableau offre donc une vue globale et actuelle des informations et statistiques des joueurs.
Les valeurs contenues dans chaque colonne peuvent être triées par ordre croissant ou décroissant, permettant ainsi de privilégier ou non certains critères de recherche.

### 5.2 Comparaison des joueurs

La partie inférieure de l'application contient plusieurs représentations plus détaillées des données. Elle permet de comparer deux joueurs entre eux selon plusieurs critères et plusieurs représentations. Cette partie est dynamique et donc premièrement composée d'un slider qui permet de sélectionner les saisons prises en compte.

La première représentation est construite sous forme de deux cartes et peuvent être vues comme des cartes de visite des joueurs. Chaque carte contient une partie supérieure statique, composée des informations générales du joueur en plus de sa photo, et une partie inférieure dynamique, composée des statistiques du joueur selon les saisons sélectionnées. Ces cartes permettent de se concentrer sur les statistiques de deux joueurs spécifiques et de les comparer rapidement à l'aide d'indicateurs visuels (flèches vertes ou rouges). Ces cartes sont représentées par l'image ci-dessous.

<img src="./readme_resources/test.jpg" alt="drawing" width="300" style="display: block; margin: 0 auto"/>

La deuxième représentation est constituée de deux scatterplot construites de manière à représenter une heatmap des tirs tentés et réussis par chacun des deux joueurs comparés. Cette représentation permet de visualiser la localisation des tirs des joueurs sur une moitié de terrain de basket-ball. Elle est composée de deux informations :
- la couleur de chaque point représente le pourcentage de réussite du joueur à cet endroit du terrain,
- la taille de chaque point représente le nombre de tirs tentés par le joueur à cet endroit du terrain.
Ces deux informations permettent de visualiser les zones de prédilection des joueurs et de comparer leur habilité aux tirs, qui est logiquement un des critères les plus importants pour un joueur de basket-ball. Cette représentation est représentée par l'image ci-dessous.

<img src="./readme_resources/test.jpg" alt="drawing" width="300" style="display: block; margin: 0 auto"/>

Comme les écarts des tirs tentés aux différents endroits peuvent être très importants (pour la plupart des joueurs, la majorité des tirs sont tentés dans la raquette, donc proche au panier), la taille des points est normalisée afin de pouvoir comparer les joueurs entre eux. La normalisation est réalisée en calculant le logarithme de base naturelle du nombre de tirs tentés à cet endroit du terrain. De cette manière, les points ne se chevauchent pas entre eux et les différences de taille sont tout de même visibles.

La dernière représentation est un line chart qui représente l'évolution des statistiques des deux joueurs au cours des saisons sélectionnées. Cette représentation permet de visualiser l'évolution des statistiques des joueurs au cours du temps et de comparer les joueurs entre eux. Cette représentation est représentée par l'image ci-dessous.

## 6. Présentation et interaction

### 6.1 Présentation

### 6.2 Interaction

## 7. Critique des outils utilisés

## 8. Conclusion