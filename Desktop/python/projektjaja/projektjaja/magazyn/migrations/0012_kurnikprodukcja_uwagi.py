# Generated by Django 4.0.4 on 2022-07-04 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazyn', '0011_alter_klient_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kurnikprodukcja',
            name='Uwagi',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
