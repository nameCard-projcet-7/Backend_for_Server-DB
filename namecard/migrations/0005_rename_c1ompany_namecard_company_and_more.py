# Generated by Django 4.2.7 on 2023-11-12 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('namecard', '0004_rename_address_namecard_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='namecard',
            old_name='C1ompany',
            new_name='Company',
        ),
        migrations.RenameField(
            model_name='namecard',
            old_name='Phonenumber',
            new_name='PhoneNumber',
        ),
    ]
