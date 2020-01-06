# Generated by Django 3.0.1 on 2020-01-05 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='contactus',
            name='phoneno',
            field=models.BigIntegerField(default=None),
        ),
    ]
