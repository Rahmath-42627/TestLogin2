# Generated by Django 5.0.6 on 2024-05-13 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vegs', '0002_rename_recepie_description_recepie_text'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recepie',
            new_name='Receipe',
        ),
    ]