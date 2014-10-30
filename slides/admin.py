from django.contrib import admin
from slides.models import Comment, User, Attachment, Slide

admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Attachment)
admin.site.register(Slide)