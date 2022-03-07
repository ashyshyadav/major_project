from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)

    def __str__(self) :
        return f"{self.user.username} Profile"