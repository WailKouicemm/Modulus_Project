# import csv
# from django.db import transaction
# from .models import Lieu, Categorie, Theme, Transport

# def import_lieux_from_csv(file_path):
#     with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
#         reader = csv.DictReader(csv_file)
#         with transaction.atomic():
#             for row in reader:
#                 nom = row['nom']
#                 description = row['description']
#                 address = row['address']
#                 latitude = float(row['latitude'])
#                 longitude = float(row['longitude'])
#                 categorie_name = row['categorie']
#                 theme_names = [theme.strip() for theme in row['theme'].split(',')]
#                 transportnames = [transport.strip() for transport in row['transport'].split(',')]
#                 categorie  = Categorie.objects.get_or_create(nom=categorie_name)
#                 themes = [Theme.objects.get_or_create(nom=theme)[0] for theme in theme_names]
#                 transports = [Transport.objects.get_or_create(nom=transport)[0] for transport in transportnames]
#                 lieu = Lieu.objects.create(
#                     nom=nom,
#                     description=description,
#                     address=address,
#                     latitude=latitude,
#                     longitude=longitude,
#                     categorie=categorie,
#                 )
#                 lieu.theme.add(themes)
#                 lieu.transport.add(transports)

#         print('Data import completed.')

# csv_file_path = 'dataset/dataset.csv'
# import_lieux_from_csv(csv_file_path)
import csv
from django.db import transaction
from .models import Lieu, Categorie, Theme, Transport

def import_lieux_from_csv(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        with transaction.atomic():
            for row in reader:
                nom = row['nom']
                description = row['description']
                address = row['address']
                latitude = float(row['latitude'])
                longitude = float(row['longitude'])
                categorie_name = row['categorie']
                theme_names = [theme.strip() for theme in row['theme'].split(',')]
                transport_names = [transport.strip() for transport in row['transport'].split(',')]
                #categorie = Categorie.objects.get_or_create(nom=categorie_name)
                themes = [Theme.objects.get_or_create(nom=theme)[0] for theme in theme_names]
                transports = [Transport.objects.get_or_create(nom=transport)[0] for transport in transport_names]
                lieu = Lieu.objects.create(
                    nom=nom,
                    description=description,
                    address=address,
                    latitude=latitude,
                    longitude=longitude,
                    categorie=Categorie.objects.get(id=1),
                )
                #lieu.theme.add(themes)
                #lieu.transport.add(transports)

        print('Data import completed.')

csv_file_path = 'dataset/dataset.csv'
import_lieux_from_csv(csv_file_path)