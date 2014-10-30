import datetime
from haystack import indexes
from slides.models import Note, RuPageModel

class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    body = indexes.CharField(model_attr='body')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Note

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

# import os
# from django.db.models import signals
# from django.conf import settings
#
# WHOOSH_SCHEMA = fields.Schema(title=fields.TEXT(stored=True),
#                               content=fields.TEXT,
#                               url=fields.ID(stored=True, unique=True))


class RuPageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, null=True)
    title = indexes.CharField(model_attr='title', null=True)
    page_url = indexes.CharField(model_attr='page_url', null=True)
    page_number = indexes.CharField(model_attr='page_number', null=True)
    page_down = indexes.CharField(model_attr='page_down', null=True)
    pub_date = indexes.DateTimeField(model_attr='pub_date', null=True)

    def get_model(self):
        return RuPageModel

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

