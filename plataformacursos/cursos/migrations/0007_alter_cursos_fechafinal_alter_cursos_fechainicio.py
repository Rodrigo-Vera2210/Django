# Generated by Django 4.2.2 on 2023-09-01 00:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0006_alter_cursos_fechafinal_alter_cursos_fechainicio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='fechaFinal',
            field=models.DateField(default=datetime.datetime(2023, 8, 31, 19, 40, 46, 744616), verbose_name='Fecha de finalización'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='fechaInicio',
            field=models.DateField(default=datetime.datetime(2023, 8, 31, 19, 40, 46, 744616), verbose_name='Fecha de inicio'),
        ),
    ]
