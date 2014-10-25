from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    image = models.ImageField(upload_to='user_photo', blank=True, null=True)
    name = models.CharField(max_length=255)

# class Attachment(models.Model):
#     pass

class Comment(models.Model):
    # attachments = models.ManyToManyField(Attachment, related_name="comments", blank=True, null=True)
    text = models.TextField()
    user = models.ForeignKey(User, related_name="comments")
    date = models.DateTimeField(auto_now_add=True)

