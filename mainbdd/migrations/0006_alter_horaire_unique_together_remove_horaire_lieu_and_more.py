# Generated by Django 4.2 on 2023-05-02 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainbdd', '0005_rename_theme_theme_lieu'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='horaire',
            unique_together={('jour', 'lieu')},
        ),
        migrations.RemoveField(
            model_name='horaire',
            name='lieu',
        ),
        migrations.AddField(
            model_name='horaire',
            name='lieu',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='horaires', to='mainbdd.lieu'),
        ),
    ]
