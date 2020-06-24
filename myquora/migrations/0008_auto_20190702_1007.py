# Generated by Django 2.2.2 on 2019-07-02 10:07

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myquora', '0007_auto_20190702_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2019, 7, 2, 10, 7, 44, 341522, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2019, 7, 2, 10, 7, 44, 341545, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2019, 7, 2, 10, 7, 44, 340298, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2019, 7, 2, 10, 7, 44, 340930, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2019, 7, 2, 10, 7, 44, 340954, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2019, 7, 2, 10, 7, 44, 342244, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2019, 7, 2, 10, 7, 44, 342268, tzinfo=utc), null=True),
        ),
    ]