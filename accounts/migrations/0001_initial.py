# Generated by Django 3.0.1 on 2020-01-01 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('roll_no', models.BigIntegerField(unique=True)),
                ('course', models.CharField(choices=[('BTECH', 'Btech'), ('MTECH', 'Mtech'), ('BCA', 'BCA'), ('MCA', 'MCA'), ('BSC', 'Bsc'), ('MSC', 'Msc'), ('MBA', 'MBA')], default='CE', max_length=10)),
                ('branch', models.CharField(choices=[('CE', 'CE'), ('IT', 'IT'), ('ECE', 'ECE'), ('ECS', 'ECS'), ('EIC', 'EIC'), ('EL', 'EL'), ('MECH', 'MECH'), ('CIVIL', 'CIVIL')], max_length=10)),
                ('icard', models.ImageField(blank=True, null=True, upload_to='icard')),
                ('phoneno', models.BigIntegerField(default=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
