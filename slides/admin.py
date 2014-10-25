from django.contrib import admin
from slides.models import Comment, User

admin.site.register(User)
admin.site.register(Comment)
