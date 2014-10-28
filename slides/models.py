from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    image = models.ImageField(upload_to='media/user_photo', blank=True, null=True)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Slide(models.Model):
    week_number = models.IntegerField()
    day = models.CharField(max_length=5)
    slide_set = models.IntegerField()
    slide_number = models.IntegerField()
    slide_header = models.CharField(max_length=255)

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, related_name="comments")
    date = models.DateTimeField(auto_now_add=True)
    # week_number = models.IntegerField()
    # day = models.CharField(max_length=5)
    # slide_set = models.IntegerField()
    # slide_number = models.IntegerField()
    slide = models.ForeignKey(Slide, related_name="comments")

    def __unicode__(self):
        return u"slide on {}".format(self.date)
# https://students.rocketu.com/week8/5_am/#/1/2
# https://students.rocketu.com/weekweek_number/day/#/slide_set/slide_number

class Attachment(models.Model):
    file = models.FileField(upload_to='media/comment_attachment', blank=True, null=True)
    uuid = models.CharField(max_length=255)
    comment = models.ForeignKey(Comment, related_name="attachments", blank=True, null=True)

    def __unicode__(self):
# https://students.rocketu.com/weekweek_number/day/#/slide_set/slide_number
        return self.file.name.split('/')[2]  #FIX and add test
