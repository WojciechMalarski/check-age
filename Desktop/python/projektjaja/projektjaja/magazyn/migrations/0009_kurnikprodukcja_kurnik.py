# Generated by Django 4.0.4 on 2022-07-03 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazyn', '0008_kurnikprodukcja_alter_klient_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kurnikprodukcja',
            name='Kurnik',
            field=models.CharField(default='', max_length=300),
        ),
    ]
