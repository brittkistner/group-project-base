from django.contrib import admin
<<<<<<< HEAD
from slides.models import Comment, User
# from rocketu.items import RocketuItem

admin.site.register(User)
admin.site.register(Comment)
# admin.site.register(RocketuItem)
=======
from slides.models import Comment, User, Attachment

admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Attachment)
>>>>>>> 24ea56b98701ebc8cf327194fc0e35970e63b2f6
