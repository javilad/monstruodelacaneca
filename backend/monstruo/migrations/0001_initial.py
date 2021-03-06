# Generated by Django 2.1 on 2018-10-31 01:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Caneca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=250)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='img/fotosapp/')),
            ],
        ),
        migrations.CreateModel(
            name='Reciclador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=20)),
                ('correo', models.CharField(blank=True, max_length=30)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='img/fotosapp/')),
                ('monedas', models.IntegerField()),
                ('puntos', models.IntegerField()),
                ('nivelActual', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Residuo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='img/fotosapp/')),
                ('descripcion', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=250)),
                ('caneca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monstruo.Caneca')),
            ],
        ),
        migrations.CreateModel(
            name='TipoReciclador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=250)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='img/fotosapp/')),
            ],
        ),
        migrations.AddField(
            model_name='reciclador',
            name='tipoReciclador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monstruo.TipoReciclador'),
        ),
        migrations.AddField(
            model_name='reciclador',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='caneca',
            name='tipoUso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monstruo.TipoUso'),
        ),
    ]
