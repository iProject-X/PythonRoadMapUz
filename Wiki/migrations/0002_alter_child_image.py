# Generated by Django 4.2.5 on 2023-09-17 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
