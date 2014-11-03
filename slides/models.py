from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    image = models.ImageField(upload_to='media/user_photo', blank=True, null=True)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.username

class Slide(models.Model):
    week_number = models.IntegerField()
    day = models.CharField(max_length=5)
    slide_set = models.IntegerField()
    slide_number = models.IntegerField()
    slide_header = models.CharField(max_length=255)
    url = models.URLField(null=True)

    def __unicode__(self):
        return 'Slide header Week: {} Day: {} Slide set: {} Slide number: {}'.format(
            self.week_number,
            self.day,
            self.slide_set,
            self.slide_number,
        )


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, related_name="comments")
    date = models.DateTimeField(auto_now_add=True)
    slide = models.ForeignKey(Slide, related_name="comments")
    # Does the comment needs these fields if it's related to a Slide?
    slide_set = models.IntegerField(null=True)
    slide_number = models.IntegerField(null=True)
    week_number = models.IntegerField(null=True)
    day = models.CharField(max_length=5)


    def slide_data(self):
        return {
            'slide_set': self.slide.slide_set,
            'slide_number': self.slide.slide_number
        }


    def __unicode__(self):
        return u"Comment on day {}, slideset {} slide number {} made on {}".format(
            self.slide.day,
            self.slide.slide_set,
            self.slide.slide_number,
            self.date
        )
# https://students.rocketu.com/week8/5_am/#/1/2
# https://students.rocketu.com/weekweek_number/day/#/slide_set/slide_number

class Attachment(models.Model):
    file = models.FileField(upload_to='media/comment_attachment', blank=True, null=True)
    uuid = models.CharField(max_length=255)
    comment = models.ForeignKey(Comment, related_name="attachments", blank=True, null=True)

    def __unicode__(self):
        return self.file.name.split('/')[2]  #FIX and add test
