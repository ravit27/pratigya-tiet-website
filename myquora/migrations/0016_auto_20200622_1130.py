# Generated by Django 2.2.5 on 2020-06-22 06:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myquora', '0015_auto_20200621_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 6, 0, 6, 61245, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 6, 0, 6, 61245, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 6, 0, 6, 57244, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 6, 0, 6, 59244, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 6, 0, 6, 59244, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 6, 0, 6, 64245, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 6, 0, 6, 64245, tzinfo=utc), null=True),
        ),
    ]