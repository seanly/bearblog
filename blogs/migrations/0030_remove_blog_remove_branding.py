# Generated by Django 3.0.7 on 2021-03-30 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0029_subscriber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='remove_branding',
        ),
    ]