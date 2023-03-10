# Generated by Django 4.0.4 on 2022-07-03 04:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazyn', '0007_suma_datazamowienia'),
    ]

    operations = [
        migrations.CreateModel(
            name='KurnikProdukcja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IloscSS', models.FloatField(default=0)),
                ('IloscS', models.FloatField(default=0)),
                ('Ilosc1A', models.FloatField(default=0)),
                ('Ilosc1B', models.FloatField(default=0)),
                ('Ilosc2A', models.FloatField(default=0)),
                ('Ilosc2B', models.FloatField(default=0)),
                ('Stloczki', models.FloatField(default=0)),
                ('Dataprodukcji', models.DateField(default=datetime.date(2022, 7, 3))),
                ('Sumaprodukcji', models.FloatField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='klient',
            name='Data',
            field=models.DateField(default=datetime.date(2022, 7, 3)),
        ),
        migrations.AlterField(
            model_name='suma',
            name='DataZamowienia',
            field=models.DateField(default=datetime.date(2022, 7, 3)),
        ),
    ]
