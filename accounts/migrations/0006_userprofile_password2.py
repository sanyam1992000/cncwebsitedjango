# Generated by Django 3.0.1 on 2020-01-03 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200103_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='password2',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
