# Generated by Django 4.2.2 on 2023-08-28 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=500)),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('portada', models.ImageField(blank=True, max_length=255, null=True, upload_to='cursos/', verbose_name='Portada')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='DetalleCursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progreso', models.IntegerField(default=0)),
                ('nota', models.IntegerField(default=0)),
                ('inscripcion', models.BooleanField(default=False)),
                ('aprobacion', models.BooleanField(default=False)),
            ],
        ),
    ]
