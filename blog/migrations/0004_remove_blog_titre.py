# Generated by Django 5.0.1 on 2024-02-04 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='titre',
        ),
    ]