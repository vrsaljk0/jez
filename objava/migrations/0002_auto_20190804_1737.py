# Generated by Django 2.2.1 on 2019-08-04 15:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('objava', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editobjave',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 4, 15, 37, 4, 58411, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='objava',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 4, 15, 37, 4, 57412, tzinfo=utc)),
        ),
    ]
