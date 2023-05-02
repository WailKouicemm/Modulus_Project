# Generated by Django 4.2 on 2023-05-02 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbdd', '0008_remove_theme_lieu_lieu_theme_alter_horaire_jour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transport',
            name='lieu',
        ),
        migrations.AddField(
            model_name='lieu',
            name='transport',
            field=models.ManyToManyField(related_name='lieux', to='mainbdd.transport'),
        ),
        migrations.AlterField(
            model_name='lieu',
            name='theme',
            field=models.ManyToManyField(related_name='lieux', to='mainbdd.theme'),
        ),
    ]
