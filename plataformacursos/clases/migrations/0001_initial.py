# Generated by Django 4.2.2 on 2023-08-28 02:18

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=200)),
                ('link_video', embed_video.fields.EmbedVideoField()),
            ],
            options={
                'verbose_name': 'Clase',
                'verbose_name_plural': 'Clases',
            },
        ),
    ]