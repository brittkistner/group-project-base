import os

PROJECT_NAME = 'lms'

AWS_ACCESS_KEY_ID = os.environ['ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['BUCKET_NAME']
STATICFILES_STORAGE = '{}.s3utils.StaticRootS3BotoStorage'.format(PROJECT_NAME)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = '//{}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)
MEDIA_URL = S3_URL + "media/"
STATIC_URL = S3_URL + "static/"
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"