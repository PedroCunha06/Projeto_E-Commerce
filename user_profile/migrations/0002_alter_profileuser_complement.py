# Generated by Django 5.0.6 on 2024-07-18 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='complement',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]