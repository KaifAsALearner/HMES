# Generated by Django 5.1.2 on 2024-10-25 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Patient',
            new_name='Patients',
        ),
    ]
