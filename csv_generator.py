import csv
import random

def generate_csv(filename, num_rows):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Écrire l'en-tête du fichier CSV
        writer.writerow(['ID', 'Nom', 'Âge', 'Ville'])
        
        # Générer des données aléatoires pour chaque ligne
        for i in range(num_rows):
            id = i + 1
            name = f"Personne {id}"
            age = random.randint(18, 60)
            city = random.choice(['Paris', 'Londres', 'New York', 'Tokyo'])
            
            # Écrire une ligne de données dans le fichier CSV
            writer.writerow([id, name, age, city])

# Appel de la fonction pour générer le fichier CSV
generate_csv('data.csv', 10000)
