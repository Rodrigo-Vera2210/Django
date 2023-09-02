# Generated by Django 4.2.2 on 2023-08-28 03:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cursos', '0003_rename_detallecursos_detallescursos_and_more'),
        ('recursos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comprobante', models.FileField(blank=True, max_length=255, null=True, upload_to='comprobantes/', verbose_name='comprobante')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('aprobado', models.BooleanField(default=False)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedidosRecursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aprobacion', models.BooleanField(default=False)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.pedidos')),
                ('recurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recursos.recursos')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedidosCursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aprobacion', models.BooleanField(default=False)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.cursos')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.pedidos')),
            ],
        ),
    ]