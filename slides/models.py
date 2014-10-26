from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    image = models.ImageField(upload_to='media/user_photo', blank=True, null=True)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Attachment(models.Model):
    file = models.ImageField(upload_to='media/comment_attachment', blank=True, null=True)
    #add guid

    def __unicode__(self):
        return self.pk


class Comment(models.Model):
    attachments = models.ForeignKey(Attachment, related_name="comments", blank=True, null=True)
    text = models.TextField()
    user = models.ForeignKey(User, related_name="comments")
    date = models.DateTimeField(auto_now_add=True)
    week_number = models.IntegerField()
    day = models.CharField(max_length=5)
    slide_set = models.IntegerField()
    slide_number = models.IntegerField()

    def __unicode__(self):
        return u"slide from week{}/{}/#/{}/{}".format(self.week_number,self.day, self.slide_set, self.slide_number)
# https://students.rocketu.com/week8/5_am/#/1/2
# https://students.rocketu.com/weekweek_number/day/#/slide_set/slide_number