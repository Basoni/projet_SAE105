import pandas as pd
import icalendar
from datetime import datetime
import matplotlib.pyplot as plt
# Charger le fichier .ics
with open('ADECal.ics', 'r') as f:
    cal = icalendar.Calendar.from_ical(f.read())

# Initialiser des listes pour stocker les détails des événements
events = []
columns = ['Type', 'Etudiants', 'Debut', 'Fin']

# Parcourir tous les événements du calendrier
for component in cal.walk():
    if component.name == "VEVENT":  # Vérifier s'il s'agit d'un événement
        # Récupérer les détails de l'événement
        start_time = component.get('DTSTART').dt
        end_time = component.get('DTEND').dt
        description = component.get('DESCRIPTION').to_ical().decode('utf-8')
        
        # Extraire le type de cours et le type d'étudiants (alternance ou formation initiale)
        if 'RT1-S2' in description:
            course_type = 'CM'
        elif 'RT1-S1' in description:
            course_type = 'CM'
        elif 'TDFourier' in description:
            course_type = 'TD'
        elif 'RT1Turing' in description:
            course_type = 'TP'       
        if 'RT1App' in description:
            student_type = 'Alternance'
        else:
            student_type = 'Formation initiale'
        
        # Ajouter les détails de l'événement à la liste
        events.append([course_type, student_type, start_time, end_time])

# Créer un DataFrame Pandas à partir des événements
df = pd.DataFrame(events, columns=columns)

# Enregistrer le DataFrame au format CSV
df.to_csv('events_processed.csv', index=False)

# Charger le fichier CSV avec les événements prétraités
df = pd.read_csv('events_processed.csv')

# Convertir les colonnes 'Debut' et 'Fin' en objets datetime
df['Debut'] = pd.to_datetime(df['Debut'])
df['Fin'] = pd.to_datetime(df['Fin'])

# Calculer la durée de chaque événement en heures
df['Duree'] = (df['Fin'] - df['Debut']).dt.total_seconds() / 3600

# Grouper par type de cours et type d'étudiants, puis calculer le volume horaire total
volume_horaire = df.groupby(['Type', 'Etudiants'])['Duree'].sum().reset_index()

# Affichage du volume horaire
print(volume_horaire)
# Grouper par type de cours et type d'étudiants, puis calculer le volume horaire total
volume_horaire = df.groupby(['Type', 'Etudiants'])['Duree'].sum().reset_index()

# Créer un diagramme à barres pour visualiser le volume horaire
plt.figure(figsize=(10, 6))
for etudiant in volume_horaire['Etudiants'].unique():
    if etudiant != 'Alternance':
        data = volume_horaire[volume_horaire['Etudiants'] == etudiant]
        plt.bar(data['Type'], data['Duree'], label=etudiant)

plt.xlabel('Type de cours')
plt.ylabel('Volume horaire (heures)')
plt.title('Volume horaire par type de cours et type d\'étudiants')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Afficher le diagramme
plt.show()
# Séparer les données en deux DataFrames : un pour l'initiale et un pour l'alternance

alternance = df[df['Etudiants'] == 'Alternance']

# Calculer le volume horaire pour chaque type d'étudiants

volume_alternance = alternance.groupby('Type')['Duree'].sum()

# Créer un diagramme à barres pour l'alternance
plt.figure(figsize=(10, 6))
plt.bar(volume_alternance.index, volume_alternance.values, color='orange')
plt.xlabel('Type de cours')
plt.ylabel('Volume horaire (heures)')
plt.title('Volume horaire par type de cours pour l\'Alternance')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

volume_horaire.to_csv('volume_horaire.csv', index=False)