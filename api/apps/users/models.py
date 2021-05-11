from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth import get_user_model


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    objects = CustomUserManager()
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    phone = models.IntegerField(default=0)
    profile_picture = models.ImageField(
        upload_to='profile_image', default='default/profile.png')
    dark_mode = models.BooleanField(default=False)

    def __str__(self):
        return self.username

User = get_user_model()
class PictureProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_image', default='default/profile.png')



    def __str__(self):
        return self.profile_image.name