# Generated by Django 3.0.4 on 2020-03-26 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viral', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='totalTestResultsIncrease',
            field=models.IntegerField(null=True),
        ),
    ]
