# Generated by Django 4.2.7 on 2023-11-12 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namecard', '0002_rename_phoneumber_namecard_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='namecard',
            name='address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='namecard',
            name='company',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='namecard',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='namecard',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='namecard',
            name='phonenumber',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='namecard',
            name='role',
            field=models.CharField(max_length=50),
        ),
    ]