# Generated by Django 3.0.1 on 2019-12-30 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20191230_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_content',
            field=models.TextField(),
        ),
    ]
