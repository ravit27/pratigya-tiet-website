# Generated by Django 2.2.5 on 2020-06-23 07:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myquora', '0016_auto_20200622_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of the sender', max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('mob', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Feedback',
            },
        ),
        migrations.DeleteModel(
            name='contact',
        ),
        migrations.AlterField(
            model_name='answer',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 6, 23, 7, 34, 5, 210285, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2020, 6, 23, 7, 34, 5, 210285, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 6, 23, 7, 34, 5, 205285, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 6, 23, 7, 34, 5, 208285, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2020, 6, 23, 7, 34, 5, 208285, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 6, 23, 7, 34, 5, 213286, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2020, 6, 23, 7, 34, 5, 213286, tzinfo=utc), null=True),
        ),
    ]
