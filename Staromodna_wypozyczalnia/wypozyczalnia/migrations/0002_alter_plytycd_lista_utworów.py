# Generated by Django 4.0.4 on 2022-05-21 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wypozyczalnia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plytycd',
            name='lista_utworów',
            field=models.TextField(blank=True, null=True),
        ),
    ]
