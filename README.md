# data-pipeline ETL simple
Objectifs
Analyse de l'humidité des sols en France de 1960 à 2024
à partir des données officielles de Météo France.

Source : Météo France (données publiques)
- Période : 1960 - 2024
- Indicateur : SWI (Soil Water Index)

Technologies utilisés
- Python / Pandas : Traitement et nettoyage des données
- Looker Studio : visualisation

- Structure du projet
- swi.0-249.csv : Données brutes Météo France ( environ 164K lignes)
- explore_date.py : Script Python de nettoyage des données
- meteo_propre.csv: Données nettoyées (60K lignes, 2000-2024)
- dashboard.pdf : Aperçu du dashboard

Le dashboard permet de : 
- Visualiser l'évolution de l'humidité dans le temps
- Comparer les stations météorologiques
- Explorer les données par année
- Localiser géographiquement les stations


Projet réalisé en Février 2026
