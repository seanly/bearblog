# Generated by Django 3.1.14 on 2024-02-07 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0100_auto_20240202_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='ignored_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]