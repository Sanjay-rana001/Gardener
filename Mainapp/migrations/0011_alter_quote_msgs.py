# Generated by Django 4.2 on 2023-05-27 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0010_alter_quote_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='msgs',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]