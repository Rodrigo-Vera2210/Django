# Generated by Django 4.2.2 on 2023-08-28 20:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2023, 8, 28, 15, 43, 23, 566402)),
        ),
    ]
