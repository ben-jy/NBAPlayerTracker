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

L'interface de notre application interactive est composé de différentes représentations. Elle est composée de deux parties principales :
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
Ces deux informations permettent de visualiser les zones de prédilection du joueurs puisque les zones dans lesquelles le joueur est le plus habile formeront un groupe de points de couleur similaire et les zones où les joueurs tentent le plus de tirs formeront un groupe de points de taille similaire. Les principes de groupement de la Gestalt telles que la proximité et la similarité sont fortement utilisés dans cette représentation. Cette représentation est représentée par l'image ci-dessous.

<img src="./readme_resources/test.jpg" alt="drawing" width="300" style="display: block; margin: 0 auto"/>

Comme les écarts des tirs tentés aux différents endroits peuvent être très importants (pour la plupart des joueurs, la majorité des tirs sont tentés dans la raquette, donc proche au panier), la taille des points est normalisée afin de pouvoir comparer les joueurs entre eux. La normalisation est réalisée en calculant le logarithme de base naturelle du nombre de tirs tentés à cet endroit du terrain. De cette manière, les points ne se chevauchent pas entre eux et les différences de taille sont tout de même visibles.

La dernière représentation est un line chart qui représente l'évolution des statistiques (par saison) des deux joueurs comparés au cours des saisons sélectionnées. Plusieurs statistiques peuvent être représentées dans ce line chart selon les besoins de l'utilisateur. Chacune des statistiques est représentées par une courbe différente, d'une couleur différente. Afin de différencier l'appartence des courbes à un joueur ou à l'autre, les courbes des deux joueurs sont représentées par des traits pleins et des traits pointillés respectivement. Cette représentation est représentée par l'image ci-dessous.

<img src="./readme_resources/test.jpg" alt="drawing" width="300" style="display: block; margin: 0 auto"/>

Les boutons servent à sélectionner les statistiques à représenter dans le line chart et leur couleur correpondent à la couleur des courbes représentées.

## 6. Présentation et interaction

### 6.1 Présentation

L'interface réalisée est construite de manière verticale. Les données globales de tous les joueurs se situent en haut de la page et offrent un aperçu rapide des informations et statistiques des joueurs. La partie inférieur de l'interface sert à analyser en détail deux joueurs qui sont comparés. Le but de cette présentation des données et de permettre à l'utilisateur dans un premier de temps de trouver rapidement des joueurs qui correspondent à ses critères de recherche (une information générale sur le joueur, une statistique, etc.) puis d'analyser ces joueurs en détail, avec l'opportunité de les comparer pour trouver la pièce manquante à son équipe. Nous avons donc une granularité de l'information qui va de l'information globale à l'information détaillée, chaque représentation étant construite pour répondre à un besoin spécifique de l'utilisateur :
- le tableau de données globales permet de trouver rapidement des joueurs qui correspondent à des critères de recherche,
- les cartes des joueurs permettent de comparer rapidement les statistiques de deux joueurs, selon une certaine période,
- les scatterplots permettent de se concentrer spécifiquement sur la localisation des tirs des joueurs, selon une certaine période,
- le line chart permet de comparer des statistiques spécifiques de deux joueurs sur plusieurs saisons, selon une certaine période.

#### 6.1.1 Choix des couleurs

Le choix des couleurs est également important, premièrement pour uniformiser le design de l'interface et deuxièmement pour permettre à la majorité des utilisateurs de distinguer les informations. 

### 6.2 Interaction

Chacune de nos représentations sont interactives, à des niveaux différents. L'interaction principale est la possiblité d'afficher les données selon une période de temps. Ces interactions sont décrites dans les sections suivantes.

#### 6.2.1 Tri des données tabulaires

Le tableau de données est triable selon chacune des colonnes. Le tri est effectué en cliquant sur le nom de la colonne. Le tri est effectué de manière croissante par défaut, mais il est possible de trier de manière décroissante en cliquant une deuxième fois sur le nom de la colonne. Il permet à l'utilisateur de privilégier un critère (une information ou une statistique) lors de la recherche d'un joueur.

#### 6.2.2 Sélection des joueurs à comparer

Le nom des joueurs affichés dans leurs cartes est un dropdown menu dans lequel il est également possible de taper le nom du joueur recherché. Cela permet à l'utilisateur de trouver rapidement le nom du joueur qu'il souhaite comparer (en ayant typiquement en amont déjà trouvé le nom du joueur grâce au tableau de données). Au démarrage de l'application, les deux joueurs affichés sont ceux qui ont le score de performance le plus élevé. À chaque fois que la sélection dans le dropdown menu est mise à jour, les cartes des joueurs ainsi que les scatterplots et le line chart sont mis à jour avec les données des joueurs sélectionnés.

#### 6.2.3 Sélection de la période de temps

Les données affichées dans les représentations de comparaison sont modifiées en fonction de la période de temps sélectionnée. Les unité de temps correspondent aux saisons NBA (2012-13, 2013-14, etc.), qui sont comprises entre la saison 2012-13 à la saison actuelle (2022-23). La période de temps est sélectionnée par un slider qui est situé en haut de la partie inférieure de l'interface. Le slider est composé de deux curseurs, un pour la période de début et un pour la période de fin. Il est représenté par l'image ci-dessous.

<img src="./readme_resources/slider.png" alt="drawing" width="300" style="display: block; margin: 0 auto"/>

Lors de sa mise à jour, les données de chacune des représentations de la partie de comparaison de l'interface (c'est-à-dire les cartes, les scatters plots et le line chart) sont mises à jour en fonction de la période de temps sélectionnée.

#### 6.2.4 Survol des points des scatterplots

Lorsque l'utilisateur survole un point sur un scatterplot, le point est mis en évidence et données précises des tirs pour la localisation en question sont affichées dans un tooltip. Le tooltip est composé de trois informations :
- le pourcentage de réussite des tirs (FG%),
- le nombre de tirs tentés (FGA),
- le nombre de tirs réussis (FGM).
Ceci permet à l'utilisateur d'avoir s'il le souhaite des informations plus précises sur les tirs des joueurs, sans pour autant péjorer la lisibilité de la représentation.

#### 6.2.5 Choix des statistiques à afficher dans le line chart

Le line chart permet l'évolution des statistiques de deux joueurs sur une certaine période. Chaque statistique peut être affichée ou non en sélectionnant ou déselectionnant le bouton (qui sert de checkbox) correspondant à la statistique. Cela permet à l'utilisateur de choisir les statistiques qu'il souhaite comparer.

## 7. Critique des outils utilisés

Tout l'application a été développée en utilisant le framework Python Dash. Ce framework étant particulièrement adapté à la création d'application web de visualisation de données, la réalisation de notre projet a été grandement facilitée et accélérée. Cependant, cette facilité d'utilisation a un coût, puisqu'il est difficile de personnaliser certains composants et donc d'implémenter des comportements spécifiques à l'utilisation que nous voulions en faire.

Nous voulions par exemple implémenter la possibilité d'ajouter des joueurs dans la comparaison en cliquant sur un bouton contenu dans le tableau de données, afin de renforcer l'idée que ce tableau sert de point de départ en amont de la comparaison. Avec Dash, il semblait difficile d'implémenter ce comportemnet et avons donc été contraint d'opter pour une utilisation plus classique avec un dropdown menu.

Notre application étant composé de visualisations de données assez classiques, nous n'avons pas eu des besoins conséquents de personnalisation et le choix de cette technologie s'est donc avéré judicieux et pertinent. Il est aussi important de noter qu'elle était nouvelle pour nous, et qu'avec un peu plus d'expérience, nous aurions pu certainement l'utiliser de manière plus efficace. 

## 8. Conclusion

En conclusion, nous avons pu réaliser un projet qui nous a permis de mettre en pratique les connaissances acquises en cours de visualisation de données tout en répondant à la problématique que nous 