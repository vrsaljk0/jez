# Generated by Django 2.2.4 on 2019-08-08 17:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('studij', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objava',
            fields=[
                ('objava_id', models.AutoField(primary_key=True, serialize=False)),
                ('tema', models.CharField(default='NN', max_length=50)),
                ('date', models.DateTimeField(default=datetime.datetime(2019, 8, 8, 17, 42, 12, 825445, tzinfo=utc))),
                ('likes', models.IntegerField(default=0)),
                ('tekst', models.TextField()),
                ('kolegij_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='studij.Kolegij')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]