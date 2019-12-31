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
    roll_no = models.IntegerField(unique=True)
    course = models.CharField(choices=courses, max_length=10, default='CE')
    branch = models.CharField(choices=branch, max_length=10)
    icard = models.ImageField(upload_to='icard', blank=True, null=True)
    phoneno = models.IntegerField(unique=True, default=None)

    def __str__(self):
        return str(self.roll_no) + ' , ' + str(self.user)
