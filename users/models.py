from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(default='default.jpg', upload_to='users_avatars/%Y/%m/%d/')

    def __str__(self):
        return self.title
