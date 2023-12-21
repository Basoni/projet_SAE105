import pandas as pd
import icalendar

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

# Charger le contenu du CSV dans un DataFrame
df = pd.read_csv('events.csv')

# Créer un masque pour les RT1App
rt1app_mask = df['Description'].str.contains('RT1App', regex=True)

# Créer un masque pour les autres cours spécifiques
other_mask = df['Description'].str.contains('RT1Huffman|TDFourier|RT1-S2|RT1-S1', regex=True)

# Créer un DataFrame séparé pour les RT1App
rt1app_courses = df[rt1app_mask]

# Créer un DataFrame séparé pour les autres cours spécifiques
other_courses = df[other_mask]

# Grouper et compter les heures pour les RT1App par événement
rt1app_hours = rt1app_courses.groupby('Événement')['Durée'].sum().reset_index()

# Grouper et compter les heures pour les autres cours spécifiques par événement
other_hours = other_courses.groupby('Événement')['Durée'].sum().reset_index()

# Afficher le total des heures pour les RT1App par cours
print("Total des heures pour RT1App par cours:")
print(rt1app_hours)

# Afficher le total des heures pour les autres cours spécifiques par cours
print("\nTotal des heures pour les autres cours spécifiques par cours:")
print(other_hours)

