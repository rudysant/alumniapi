from django.db import models
from django.contrib.auth.models import AbstractUser

class AlumniUser(AbstractUser):
    fullname = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.fullname

