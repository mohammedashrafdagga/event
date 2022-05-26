from django.db import models

# Create your models here.


class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=120, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    pssword = models.CharField(max_length=16)

    def __str__(self):
        return str(f'{self.first_name} {self.last_name}')
