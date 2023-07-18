# Hadoop / Spark

## Génération des données

Récupérer le script python de génération de données

`wget ...`

Exécuter le script

`python3 csv_generator.py`

## Stockage des données dans Hadoop

Copier le fichier data.csv précédement generé dans le système de fichier d'Hadoop

`hdfs dfs -moveFromLocal data.csv /m2i`

## Exécution du script de récupération de données avec Spark

Récupérer le script python pour Spark

`wget ...`

Exécuter le script avec Spark

`/opt/spark/bin/spark-submit check-data.py`
