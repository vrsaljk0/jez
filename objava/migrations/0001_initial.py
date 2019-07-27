# Generated by Django 2.2.3 on 2019-07-27 17:21

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('studij', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objava',
            fields=[
                ('objava_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=datetime.datetime(2019, 7, 27, 17, 21, 34, 33793, tzinfo=utc))),
                ('likes', models.IntegerField(default=0)),
                ('allow_edit', models.BooleanField(default=False)),
                ('tekst', models.TextField()),
                ('kolegij_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='studij.Kolegij')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.Student')),
            ],
        ),
        migrations.CreateModel(
            name='EditObjave',
            fields=[
                ('edit_objave_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=datetime.datetime(2019, 7, 27, 17, 21, 34, 34599, tzinfo=utc))),
                ('objava_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='objava_id_fk', to='objava.Objava')),
                ('tekst', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tekst_id_fk', to='objava.Objava')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.Student')),
            ],
        ),
    ]