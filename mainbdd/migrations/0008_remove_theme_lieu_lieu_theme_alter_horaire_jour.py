# Generated by Django 4.2 on 2023-05-02 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbdd', '0007_alter_horaire_lieu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='lieu',
        ),
        migrations.AddField(
            model_name='lieu',
            name='theme',
            field=models.ManyToManyField(related_name='themes', to='mainbdd.theme'),
        ),
        migrations.AlterField(
            model_name='horaire',
            name='jour',
            field=models.CharField(choices=[('Lundi', 'Lundi'), ('Mardi', 'Mardi'), ('Mercredi', 'Mercredi'), ('Jeudi', 'Jeudi'), ('Vendredi', 'Vendredi'), ('Samedi', 'Samedi'), ('Dimanche', 'Dimanche')], max_length=10),
        ),
    ]