# Generated by Django 4.2.2 on 2023-08-28 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clases', '0001_initial'),
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clases',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.cursos'),
        ),
    ]
