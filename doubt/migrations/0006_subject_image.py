# Generated by Django 3.1.4 on 2020-12-08 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doubt', '0005_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='image',
            field=models.ImageField(default='', upload_to='doubt/images'),
        ),
    ]