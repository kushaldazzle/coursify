# Generated by Django 3.1.4 on 2020-12-08 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doubt', '0006_subject_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='doubtquestion',
            name='image',
            field=models.ImageField(default='', upload_to='doubt/post'),
        ),
    ]