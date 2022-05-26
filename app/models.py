from django.db import models
from userp.models import Profile
# Create your models here.


class EventObj(models.Model):
    host = models.ForeignKey(Profile, on_delete=models.CASCADE)
    event_username = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    descripations = models.TextField(blank=True, null=False)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return str(f'{self.title}')


class SubEventObj(models.Model):
    in_event = models.ForeignKey(EventObj, on_delete=models.CASCADE)
    serial_subevent = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    descripations = models.TextField(blank=True, null=False)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_offline = models.BooleanField(default=True)
    guest_user = models.CharField(max_length=250)

    def __str__(self):
        return str(f'{self.title}')
