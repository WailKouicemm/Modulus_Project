# Generated by Django 4.2 on 2023-06-16 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbdd', '0030_alter_lieu_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='nom',
            field=models.CharField(choices=[('musé', 'musé'), ('plage', 'plage'), ('forét', 'forét'), ('ville', 'ville'), ('montagne', 'montagne'), ('campagne', 'campagne'), ('lac', 'lac'), ('rivière', 'rivière'), ('désert', 'désert'), ('grotte', 'grotte'), ('falaise', 'falaise'), ("chute d'eau", "chute d'eau"), ('mosqué', 'mosqué')], max_length=50, unique=True),
        ),
    ]
