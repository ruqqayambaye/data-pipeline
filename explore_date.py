#projet pipeline ETL + data visualisation
# @author: Rokhaya MBAYE
# 1. Tu importes de la librairie pandas
import pandas as pd;

# 2. Lecture et stcokage du fichier csv dans une variable
data = pd.read_csv('/home/rokina/Documents/Projet Perso/Pipeline-donées/Dataset/swi.0000-0249/swi.0-249.csv', sep =";");

# Affcihages des premiers lignes pour s'assurer quele fichier est bien lu 
print(data.head());  

# Suppression des lignes vides
data = data.dropna();

# Suppressions les doublons
data = data.drop_duplicates();

# Affichage des colonnes du dataset
print(data.columns.tolist());

#Transformation de l'indice d'humidité de String vers flottant ^pour éviter des soucis lors de la création du tableau de bord
data['SWI_UNIF_MENS'] = data['SWI_UNIF_MENS'].str.replace(',', '.').astype(float);

# Sauvegarde fu fichier version nettoyé qui sera utilisé pour la création du tableau de bord
data.to_csv('meteo_propre.csv', index=False, sep = ';');

# Affichage du dataframe après nettoyage
print(data.info());

# Affcihage des statistiques de base
print(data.describe());

# Affichage du nombre de valeurs manquantes par colonne
print(data.isnull().sum());

