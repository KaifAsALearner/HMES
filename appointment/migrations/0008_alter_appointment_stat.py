# Generated by Django 5.1.2 on 2024-11-02 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0007_appointment_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='stat',
            field=models.CharField(choices=[('CONFIRMED', 'Confirmed'), ('CANCELLED', 'Cancelled'), ('COMPLETED', 'Completed')], default='CONFIRMED', max_length=20),
        ),
    ]