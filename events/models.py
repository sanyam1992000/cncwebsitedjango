from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    certi_description = RichTextUploadingField(blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    venue = models.CharField(max_length=100, default=None, blank=True, null=True)
    pic1 = models.ImageField(default=None, upload_to='event pics')
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
    status = models.CharField(default=True, choices=(('True', 'Upcoming'), ('False', 'Happened')), max_length=10)

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse('events:events_detail', args=[str(self.pk)])

    class Meta:
        ordering = ['-date']


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='registrations')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    attended = models.CharField(choices=(('A', 'Attended'), ('NA', 'Not Attended')), max_length=10, default='NA')

    def __str__(self):
        return self.event.event_name + self.user.username

    def is_user_registered_for_event(self, user, event):
        if self.objects.get(user=user, event=event):
            return True
        else:
            return False

    class Meta:
        ordering = ['-date']


class Institute(models.Model):
    institute = models.CharField(max_length=100)
    previous_events = RichTextUploadingField(blank=True, null=True)
    contact_person = models.CharField(max_length=1000, blank=True, null=True)
    contact_person_phone_number = models.BigIntegerField(blank=True, null=True)
    email = models.EmailField(max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return self.institute

    class Meta:
        ordering = ['institute']