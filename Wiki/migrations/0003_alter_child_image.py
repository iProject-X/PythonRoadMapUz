# Generated by Django 4.2.5 on 2023-09-17 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wiki', '0002_alter_child_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
