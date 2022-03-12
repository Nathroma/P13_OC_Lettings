# P13_OC_Lettings

## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## Déploiement de l'application avec circleCI

Dans le cas ou le code est mis à jour sur github (plus précisément sur la branche master) CircleCi va récuperer ce code et lancer une série de commande visant:
- A vérifier le code 
- Effectuer des tests 
- Verifier le linting
- Le déployer sur Heroku 

Lien vers le pipeline CircleCI : [Cliquez ici](https://app.circleci.com/pipelines/github/Nathroma/P13_OC_Lettings?branch=master&filter=all)

Il est nécessaire de posséder des comptes sur les platformes suivantes :
- DockerHub
- CircleCI
- Heroku

### Installation 
- Créer un projet DockerHub
- Créer un projet sur CircleCi puis le lier a un dépot Github
- Créer un projet sur Heroku et récuperer un token d'accés à votre compte
- Ecrire les variables d'environnement des compte et clé d'accés

Une fois terminer le code se mettra automatiquement à jour sur CircleCI à chaque commit sur la branche master de Github
L'application sera ensuite disponible sur Heroku en utilisant le bouton "Open App"

## Docker

Pour récuperer une image sur DockerHub, exécutez dans un terminal 
- `docker pull user/repo_name:tag`
- `docker run -p 8000:8000 -it user/repo_name`

Ensuite rendez-vous sur l'adresse [localhost:8000](http://localhost:8000)
Docker renverra toutes les infos de management via Docker Desktop dans la rubrique Containers/Apps

## Variables d'environnement 

Les variables d'environnement sont des données qui ne doivent pas être visible par les utilisateurs par soucis de sécurité
Elles sont donc placées dans des fichiers ou paramètre de projet

Dans un fichier **.env** situé dans le dossier de l'application avec le fichier **settings.py**
**\OC_Lettings\OC_Lettings**

Dans les variables d'environnement de CircleCI affiliées au projet

| Variable | Description |
| :--------------: | :--------------: |
| SECRET_KEY | Clé de django |
| SENTRY_KEY | dsn pour Sentry |
| DEBUG | Etat du debugger |

## Sentry

### Prérequis

- Compte [Sentry](https://sentry.io/)

### Installation

- Créer un projet sur Sentry
- Récuperer le **dsn** obtenue via le projet sentry et l'ajouter aux variables d'environnement