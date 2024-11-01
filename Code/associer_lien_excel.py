# -*- coding: utf-8 -*-
"""Associer_Lien_Excel.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hk4sR5qNH9Wl4e25ZBn2vRU_eFEh3_PY
"""

# Monter Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/Sujet1NLP3D

# Étape 2: Importer les bibliothèques nécessaires
import os
import openpyxl
from google.oauth2 import service_account
from googleapiclient.discovery import build
import re

# Chemin vers votre fichier JSON d'identification OAuth 2.0
SERVICE_ACCOUNT_FILE = 'custom-casing-434908-n5-4d3c56433812.json'

# Créer les credentials pour l'API Google Drive
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=['https://www.googleapis.com/auth/drive']
)

# Créer le service Google Drive
service = build('drive', 'v3', credentials=creds)

# Étape 3: Charger le fichier Excel
file_path = 'arxiv_data.xlsx'
wb = openpyxl.load_workbook(file_path)
ws = wb.active

# Étape 4: Lister les fichiers txt

# Fonction pour extraire le numéro d'article
def extract_number(file_name):
    match = re.search(r'(\d+)', file_name)
    return int(match.group(1)) if match else -1

# Dossier contenant les fichiers txt
txt_folder = 'segmented_files/'

# Lister et trier les fichiers en fonction du numéro extrait
files = sorted(os.listdir(txt_folder), key=extract_number)

# Étape 5: Récupérer les liens de partage Google Drive pour chaque fichier
def get_shareable_link(file_name):
    results = service.files().list(q=f"name = '{file_name}'", fields="files(id, webViewLink)").execute()
    items = results.get('files', [])
    if not items:
        print(f"Fichier {file_name} introuvable.")
        return None
    else:
        # Rendre le fichier accessible via un lien
        file_id = items[0]['id']
        service.permissions().create(fileId=file_id, body={'type': 'anyone', 'role': 'reader'}).execute()
        return items[0].get('webViewLink')

# Étape 6: Associer les fichiers txt aux cellules du fichier Excel
for idx, file in enumerate(files):
    if file.endswith(".txt"):
        # Extraire le numéro de l'article à partir du nom du fichier
        article_number = file.split('_')[1].split('.')[0]
        file_name = f'article_{article_number}_segmented.txt'

        # Récupérer le lien de partage pour chaque fichier .txt
        link = get_shareable_link(file_name)

        if link:
            # Mettre à jour la cellule du contenu avec le lien
            ws[f'H{idx + 2}'] = link  # Supposant que les liens sont dans la colonne F

# Étape 7: Sauvegarder le fichier Excel mis à jour
wb.save('votre_fichier_mis_a_jour.xlsx')