# Generated by Django 4.2 on 2023-05-10 13:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbdd', '0016_alter_transport_nom'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 13, 37, 44, 589400, tzinfo=datetime.timezone.utc)),
        ),
    ]
