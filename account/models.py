from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    personal_photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, default='user_default.png')
    personal_background = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, default='background_default.png')
    
    def __str__(self):
        return self.user.username