# Generated by Django 4.2.7 on 2023-11-23 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namecard', '0011_remove_post_image_remove_post_title_post_file_dated_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media/images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
