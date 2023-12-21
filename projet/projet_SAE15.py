"""
import icalendar

# Charger le fichier .ics
with open('ADECal.ics', 'rb') as f:
    cal = icalendar.Calendar.from_ical(f.read())
#print(cal)
# Parcourir tous les événements du calendrier
for component in cal.walk():
    if component.name == "VEVENT":  # Vérifier s'il s'agit d'un événement
        # Récupérer les détails de l'événement
        summary = component.get('summary')
        start_time = component.get('dtstart').dt
        end_time = component.get('dtend').dt
        
        # Récupérer les autres informations spécifiques
        location = component.get('LOCATION')
        #professor = component.get('organizer')
        class_associated = component.get('DESCRIPTION')
        
        # Faire quelque chose avec ces détails
        print(f"Événement : {summary}")
        print(f"Début : {start_time}")
        print(f"Fin : {end_time}")
        print(f"Salle : {location}")
        #print(f"Professeur : {professor}")
        print(f"Classe : {class_associated}")
        print("\n")


import icalendar
import re

# Charger le fichier .ics
with open('ADECal.ics', 'rb') as f:
    cal = icalendar.Calendar.from_ical(f.read())

# Parcourir tous les événements du calendrier
for component in cal.walk():
    if component.name == "VEVENT":  # Vérifier s'il s'agit d'un événement
        # Récupérer les détails de l'événement
        summary = component.get('summary')
        start_time = component.get('dtstart').dt
        end_time = component.get('dtend').dt
        
        # Récupérer les autres informations spécifiques
        location = component.get('LOCATION')
        description = component.get('DESCRIPTION')
        
        # Utiliser une expression régulière pour séparer la classe du professeur
        match = re.match(r'(RT|TD|TP|LP)(.*)', description)
        if match:
            class_associated = match.group(1)
            professor = match.group(2).strip()  # Séparation du professeur
            
            # Faire quelque chose avec ces détails
            print(f"Événement : {summary}")
            print(f"Début : {start_time}")
            print(f"Fin : {end_time}")
            print(f"Salle : {location}")
            print(f"Classe : {class_associated}")
            print(f"Professeur : {professor}")
            print("\n")

"""
"""
import pandas as pd
import icalendar

# Charger le fichier .ics
with open('ADECal.ics', 'rb') as f:
    cal = icalendar.Calendar.from_ical(f.read())

# Initialiser des listes pour stocker les détails des événements
events = []
columns = ['Événement', 'Début', 'Fin', 'Description', 'LOCATION']

# Parcourir tous les événements du calendrier
for component in cal.walk():
    if component.name == "VEVENT":  # Vérifier s'il s'agit d'un événement
        # Récupérer les détails de l'événement
        summary = component.get('summary')
        start_time = component.get('dtstart').dt
        end_time = component.get('dtend').dt
        description = component.get('DESCRIPTION')
        salle = component.get('LOCATION')
        # Ajouter les détails de l'événement à la liste
        events.append([summary, start_time, end_time, description, salle])

# Créer un DataFrame Pandas à partir des événements
df = pd.DataFrame(events, columns=columns)

# Enregistrer le DataFrame au format CSV
df.to_csv('events.csv', index=False)

# Afficher le contenu du CSV
print(df)



"""
"""
import pandas as pd
import icalendar
import re


# Charger le fichier .ics
with open('ADECal.ics', 'rb') as f:
    cal = icalendar.Calendar.from_ical(f.read())

# Initialiser des listes pour stocker les détails des événements
events = []
columns = ['Événement', 'LOCATION', 'Début', 'Fin', 'Description']

# Parcourir tous les événements du calendrier
for component in cal.walk():
    if component.name == "VEVENT":  # Vérifier s'il s'agit d'un événement
        # Récupérer les détails de l'événement
        summary = component.get('summary')
        start_time = component.get('dtstart').dt
        end_time = component.get('dtend').dt
        description = component.get('DESCRIPTION')
        salle = component.get('LOCATION')
        # Ajouter les détails de l'événement à la liste
        events.append([summary, start_time, end_time, description, salle])

# Créer un DataFrame Pandas à partir des événements
df = pd.DataFrame(events, columns=columns)

# Enregistrer le DataFrame au format CSV
df.to_csv('events.csv', index=False)

# Afficher le contenu du CSV
#print(pd.read_csv('events.csv'))

# Charger le contenu du CSV dans un DataFrame
df = pd.read_csv('events.csv')
# Diviser la colonne Description en plusieurs sous-colonnes en utilisant \n comme séparateur
new_columns = df['Description'].str.split('\n', expand=True)

# Ajouter les nouvelles colonnes au DataFrame existant
df = pd.concat([df, new_columns], axis=1)



# Ajuster les paramètres d'affichage pour montrer toutes les lignes et colonnes
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# Charger le contenu du CSV dans un DataFrame
df = pd.read_csv('events.csv')

# Filtrer les lignes en fonction des descriptions spécifiques
filter_condition = df['Description'].str.contains('RT1App|RT1|RT1Shannon|RT1Huffman|RT1Turing|TDFourier|TDBell', regex=True)
filtered_df = df[filter_condition]


# Fonction pour nettoyer la colonne Description
def clean_description(text):
    matches = re.findall(r'\b(?:RT1App|RT1|RT1Shannon|RT1Huffman|RT1Turing|TDFourier|TDBell)\b.*', text)
    return ', '.join(matches)

# Appliquer la fonction à la colonne Description
df['Description'] = df['Description'].apply(clean_description)

# Diviser la colonne Description en plusieurs sous-colonnes en utilisant \n comme séparateur
new_columns = df['Description'].str.split('\n', expand=True)
df = pd.concat([df, new_columns], axis=1)

# Retirer les caractères \n des colonnes du DataFrame filtré
filtered_df = filtered_df.apply(lambda x: x.str.replace('\n', ' '))

# Afficher le contenu complet du DataFrame filtré
print(filtered_df)


"""

"""

import pandas as pd
import icalendar
import re


# Charger le fichier .ics
with open('ADECal.ics', 'rb') as f:
    cal = icalendar.Calendar.from_ical(f.read())

# Initialiser des listes pour stocker les détails des événements
events = []
columns = ['Événement', 'Début', 'Fin', 'Description', 'LOCATION']

# Parcourir tous les événements du calendrier
for component in cal.walk():
    if component.name == "VEVENT":  # Vérifier s'il s'agit d'un événement
        # Récupérer les détails de l'événement
        summary = component.get('summary')
        start_time = component.get('dtstart').dt
        end_time = component.get('dtend').dt
        description = component.get('DESCRIPTION')
        salle = component.get('LOCATION')
        # Ajouter les détails de l'événement à la liste
        events.append([summary, start_time, end_time, description, salle])

# Créer un DataFrame Pandas à partir des événements
df = pd.DataFrame(events, columns=columns)

# Enregistrer le DataFrame au format CSV
df.to_csv('events.csv', index=False)

# Afficher le contenu du CSV
#print(pd.read_csv('events.csv'))

# Charger le contenu du CSV dans un DataFrame
df = pd.read_csv('events.csv')
# Diviser la colonne Description en plusieurs sous-colonnes en utilisant \n comme séparateur
new_columns = df['Description'].str.split('\n', expand=True)


# Ajouter les nouvelles colonnes au DataFrame existant
df = pd.concat([df, new_columns], axis=1)



# Ajuster les paramètres d'affichage pour montrer toutes les lignes et colonnes
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# Charger le contenu du CSV dans un DataFrame
df = pd.read_csv('events.csv')

# Filtrer les lignes en fonction des descriptions spécifiques
filter_condition = df['Description'].str.contains('RT1App|RT1|RT1Shannon|RT1Huffman|RT1Turing|TDFourier|TDBell', regex=True)
filtered_df = df[filter_condition]


# Fonction pour nettoyer la colonne Description
def clean_description(text):
    matches = re.findall(r'\b(?:RT1App|RT1|RT1Shannon|RT1Huffman|RT1Turing|TDFourier|TDBell)\b.*', text)
    return ', '.join(matches)

# Appliquer la fonction à la colonne Description
df['Description'] = df['Description'].apply(clean_description)

# Diviser la colonne Description en plusieurs sous-colonnes en utilisant \n comme séparateur
new_columns = df['Description'].str.split('(', expand=True)
df = pd.concat([df, new_columns], axis=1)

# Retirer les caractères \n des colonnes du DataFrame filtré
filtered_df = filtered_df.apply(lambda x: x.str.replace('\n', ' '))


# Afficher le contenu complet du DataFrame filtré
print(filtered_df)




"""


import pandas as pd
import icalendar

# Charger le fichier .ics
with open('ADECal.ics', 'rb') as f:
    cal = icalendar.Calendar.from_ical(f.read())

# Initialiser des listes pour stocker les détails des événements
events = []
columns = ['Événement', 'Début', 'Fin', 'Description']

# Parcourir tous les événements du calendrier
for component in cal.walk():
    if component.name == "VEVENT":  # Vérifier s'il s'agit d'un événement
        # Récupérer les détails de l'événement
        summary = component.get('summary')
        start_time = component.get('dtstart').dt
        end_time = component.get('dtend').dt
        description = component.get('DESCRIPTION')
        # Ajouter les détails de l'événement à la liste
        events.append([summary, start_time, end_time, description])

# Créer un DataFrame Pandas à partir des événements
df = pd.DataFrame(events, columns=columns)

# Calculer la durée des événements (en heures)
df['Durée'] = (df['Fin'] - df['Début']).dt.total_seconds() / 3600

# Séparer les événements pour RT1App et les autres cours
rt1app_events = df[df['Événement'].str.contains('RT1App')]
other_events = df[~df['Événement'].str.contains('RT1App')]

# Calculer les heures pour les événements RT1App et les autres cours
rt1app_hours = rt1app_events.groupby('Événement')['Durée'].sum().reset_index()
other_hours = other_events.groupby('Événement')['Durée'].sum().reset_index()

print("Heures pour les événements RT1App :\n", rt1app_hours)
print("\nHeures pour les autres événements :\n", other_hours)
