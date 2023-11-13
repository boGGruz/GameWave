from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import random


def generate_random_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to='profile_pics')
    nickname_color = models.CharField(max_length=7, default=generate_random_color)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
