# Generated by Django 4.2.5 on 2023-10-02 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_xlsx', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosxlsx',
            name='cedula',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
