# Generated by Django 2.1 on 2018-11-16 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monstruo', '0005_auto_20181115_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciclador',
            name='tipoReciclador',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='monstruo.TipoReciclador'),
        ),
    ]