# Generated by Django 2.2.3 on 2019-07-25 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studij', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kolegij',
            name='kolegij_ime',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='studij',
            name='studij_ime',
            field=models.CharField(max_length=60),
        ),
    ]
