from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

courses = (
    ('BTECH', 'Btech'),
    ('MTECH', 'Mtech'),
    ('BCA', 'BCA'),
    ('MCA', 'MCA'),
    ('BSC', 'Bsc'),
    ('MSC', 'Msc'),
    ('MBA', 'MBA'),
    ('BBA', 'BBA'),
)

branch = (
    ('CE', 'CE'),
    ('IT', 'IT'),
    ('ECE', 'ECE'),
    ('ECS', 'ECS'),
    ('EIC', 'EIC'),
    ('EL', 'EL'),
    ('MECH', 'MECH'),
    ('CIVIL','CIVIL'),
    ('Mathematics', 'Mathematics'),
    ('Chemistry','Chemistry'),
    ('Physics','Physics'),
    ('Animation','Animation'),
    ('Others','Others'),

)

faculty_position = (
    ('Head', '1-Head'),
    ('Member', '2-Member'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(default='student pics/default_user.png', upload_to='student pics', blank=True, null=True)
    roll_no = models.BigIntegerField(unique=True)
    course = models.CharField(choices=courses, max_length=50)
    branch = models.CharField(choices=branch, max_length=50)
    icard = models.ImageField(upload_to='icard', blank=True, null=True)
    phoneno = models.BigIntegerField(default=None)

    def __str__(self):
        return str(self.user) + ' ' + str(self.roll_no)
    
    def get_absolute_url(self):
        return reverse('accounts:dashboard', args=[str(self.user.username)])
    
    class Meta:
        ordering = ['-roll_no', 'branch', 'course']


class FacultyProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pic = models.ImageField(default=None, upload_to='faculty pics', blank=True, null=True)
    department = models.CharField(max_length=20)
    position = models.CharField(choices=faculty_position, max_length=20)

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('accounts:dashboard', args=[str(self.user.username)])
    
    class Meta:
        ordering = ['position']
