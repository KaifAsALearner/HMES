# Generated by Django 5.1.2 on 2024-11-01 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_doctor_dayofstarting'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='Awards',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='Bio',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='avatar',
            field=models.ImageField(default='default_doctor_image.jpeg', upload_to=''),
        ),
    ]