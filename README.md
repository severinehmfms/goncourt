
Titre : Évaluation Python (Phase métier : Concevoir et développer la couche métier d’une application)
Sujet : prix Goncourt 2026

Auteur : Séverine Hori Maitrehut

Description : 
Ce programme permet de répondre à l'exercice donné pour l'Evaluation Python.
La consigne était de concevoir une application pour le Prix Goncourt 2026. L'application, qui ne gère dans un premier temps pas l'authentification, doit permettre à un visiteur, ou un utilisateur connecté de voir les livres qui ont été sélectionnés pour la 1ère, 2ème et 3ème sélection. Ils peuvent aussi visualiser la liste des membres du jury et de leur Président.
Dans l'avenir, l'application permettra également aux membres du jury de voter pour les livres de la deuxième puis de la troisième sélection, ainsi que pour le lauréat. Pour l'instant cette application ne le permet pas.
Le président doit pouvoir pour la deuxième sélection, choisir les 8 livres qui auront été sélectionnés ; puis pour la troisième sélection, choisir les 4 livres restants. A l'issue de ces deux sélections, il doit pouvoir noter le nombre de votes par livre pour les 4 restants, et choisir le lauréat en fonction de ces votes.

Installation : 
Pour faire fonctionner cette application, il faut au préalable :
- Créer une base de données mariaDB ou mySql.
- Importer le fichier sql/init.sql pour avoir les données de base
- Les paramètres de cette base de données sont à spécifier dans le fichier daos/dao.py 


