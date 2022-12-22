### Lancement de l'application en local

Dans le cas où l'application déployée ne serait plus accessible, il est toujours possible de lancer l'application en local. Les prérequis sont les suivants :

- Python 3.9

Ensuite, il suffit de suivre les étapes suivantes :

1. Cloner le dépôt git et se déplacer dans le dossier `code` du projet :
    
        git clone https://github.com/ben-jy/VI_NBAPlayerTracker
        cd code

2. Installer les librairies nécessaires (il est recommandé d'utiliser et activer un [environnement virtuel](https://docs.python.org/fr/3/tutorial/venv.html)) :
    
        pip install -r requirements.txt

3. Lancer ensuite l'application :

        python app.py

4. L'application est ensuite accessible à l'adresse [http://127.0.0.1:8050](http://127.0.0.1:8050).

