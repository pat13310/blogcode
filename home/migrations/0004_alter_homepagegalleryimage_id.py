# Generated by Django 5.0.1 on 2024-02-04 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepagegalleryimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagegalleryimage',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
