# Generated by Django 2.2.10 on 2020-12-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_auditions_wa_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditions',
            name='roll_no',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
