# Generated by Django 4.2.2 on 2023-09-01 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0007_alter_cursos_fechafinal_alter_cursos_fechainicio'),
        ('clases', '0004_remove_clases_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallemodulo',
            name='curso',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='cursos.cursos'),
            preserve_default=False,
        ),
    ]