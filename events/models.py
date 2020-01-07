from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    content = models.TextField(max_length=5000, blank=True, null=True)
    date = models.DateField()
    pic1 = models.ImageField(default=None, upload_to='event pics', blank=True, null=True)
    pic2 = models.ImageField(default=None, upload_to='event pics', blank=True, null=True)
    pic3 = models.ImageField(default=None, upload_to='event pics', blank=True, null=True)
    pic4 = models.ImageField(default=None, upload_to='event pics', blank=True, null=True)
    pic5 = models.ImageField(default=None, upload_to='event pics', blank=True, null=True)
    pic6 = models.ImageField(default=None, upload_to='event pics', blank=True, null=True)
    pic7 = models.ImageField(default=None, upload_to='event pics', blank=True, null=True)
    pic8 = models.ImageField(default=None, upload_to='event pics', blank=True, null=True)
    pic9 = models.ImageField(default=None, upload_to='event pics', blank=True, null=True)
    pic10 = models.ImageField(default=None, upload_to='event pics', blank=True, null=True)
    pic11 = models.ImageField(default=None, upload_to='event pics', blank=True, null=True) ##for home only
    status = models.CharField(choices=(('True', 'Upcoming'), ('False', 'Happened')), max_length=10)

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse('blog:detail', self.id)

    class Meta:
        ordering = ['-date']


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='registrations')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    attended = models.CharField(choices=(('A', 'Attended'), ('NA', 'Not Attended')), max_length=10, default='NA')

    def __str__(self):
        return self.event.event_name + self.user.username

    def is_user_registered_for_event(self,user,event):
        if self.objects.get(user=user,event=event):
            return True
        else:
            return False

    class Meta:
        ordering = ['-date']


class RequestedEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pass