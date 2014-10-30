from django.contrib import admin
from slides.models import Comment, User, Attachment, Slide
from slides.models import Comment, User, Attachment, RuPageModel, Note

admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Attachment)
admin.site.register(Slide)
admin.site.register(RuPageModel)
admin.site.register(Note)
