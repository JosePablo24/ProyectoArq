# Generated by Django 2.2.1 on 2019-07-02 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rfid', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfid',
            name='identificador',
            field=models.IntegerField(default=0),
        ),
    ]
