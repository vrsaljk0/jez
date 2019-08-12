# Generated by Django 2.2.4 on 2019-08-11 17:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('studij', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objava',
            fields=[
                ('objava_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=datetime.datetime(2019, 8, 11, 17, 43, 33, 406485, tzinfo=utc))),
                ('attachment', models.FileField(blank=True, null=True, upload_to='objava_att')),
                ('tekst', models.TextField()),
                ('kolegij_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='studij.Kolegij')),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tema.Tema')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Objava_Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objava_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='objava.Objava')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
