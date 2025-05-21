from django.db import models
from django.contrib.auth.hashers import make_password

class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    mail = models.EmailField(null=True, blank=True)
    social_media = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk or CustomUser.objects.get(pk=self.pk).password != self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
