# Generated by Django 5.1.2 on 2024-10-28 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_alter_patient_user_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='user_info',
            new_name='user',
        ),
    ]
