# Generated by Django 5.1.2 on 2024-11-01 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_alter_appointment_doctorsnote'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
