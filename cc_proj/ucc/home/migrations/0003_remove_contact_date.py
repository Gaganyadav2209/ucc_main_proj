# Generated by Django 4.1.7 on 2023-02-26 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_phone_contact_password_remove_contact_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
    ]
