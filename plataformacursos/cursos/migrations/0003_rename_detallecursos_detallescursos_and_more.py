# Generated by Django 4.2.2 on 2023-08-28 03:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cursos', '0002_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DetalleCursos',
            new_name='DetallesCursos',
        ),
        migrations.AlterModelOptions(
            name='detallescursos',
            options={'verbose_name': 'Detalle Curso', 'verbose_name_plural': 'Detalle Cursos'},
        ),
    ]
