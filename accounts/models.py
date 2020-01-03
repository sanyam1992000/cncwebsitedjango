from django.db import models
from django.contrib.auth.models import User
# Create your models here.

courses = (
    ('BTECH', 'Btech'),
    ('MTECH', 'Mtech'),
    ('BCA', 'BCA'),
    ('MCA', 'MCA'),
    ('BSC', 'Bsc'),
    ('MSC', 'Msc'),
    ('MBA', 'MBA'),
)

branch = (
    ('CE', 'CE'),
    ('IT', 'IT'),
    ('ECE', 'ECE'),
    ('ECS', 'ECS'),
    ('EIC', 'EIC'),
    ('EL', 'EL'),
    ('MECH', 'MECH'),
    ('CIVIL', 'CIVIL'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(default=None, upload_to='Student pics', blank=True, null=True)
    roll_no = models.BigIntegerField(unique=True)
    course = models.CharField(choices=courses, max_length=10, default='CE')
    branch = models.CharField(choices=branch, max_length=10)
    icard = models.ImageField(upload_to='icard', blank=True, null=True)
    phoneno = models.BigIntegerField(default=None)
    password2 = models.CharField(default=None, max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.user)


class FacultyProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    pic = models.ImageField(default=None, upload_to='Faculty pics')

    def __str__(self):
        return str(self.user)