# Generated by Django 4.2 on 2023-05-12 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainbdd', '0021_user_groups_user_user_permissions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transport',
            name='description',
        ),
    ]
