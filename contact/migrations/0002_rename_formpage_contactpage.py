# Generated by Django 5.0.1 on 2024-02-05 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FormPage',
            new_name='ContactPage',
        ),
    ]