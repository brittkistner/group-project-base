# -*- coding: utf-8 -*-

# Scrapy settings for rocketu project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'rocketu'

SPIDER_MODULES = ['rocketu.spiders']
NEWSPIDER_MODULE = 'rocketu.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'rocketu (+http://www.yourdomain.com)'

#
# def setup_django_env(path):
#     import imp, os
#     from django.core.management import setup_environ
#
#     f, filename, desc = imp.find_module('settings', [path])
#     project = imp.load_module('settings', f, filename, desc)
#
#     setup_environ(project)
#
#     # Add django project to sys.path
#     import sys
#     sys.path.append(os.path.abspath(os.path.join(path, os.path.pardir)))
#
#     setup_django_env('/path/to/django/myproject/myproject/')

#
# ITEM_PIPELINES = [
#   'scrapyelasticsearch.ElasticSearchPipeline',
# ]
#
# ELASTICSEARCH_SERVER = 'localhost'
# ELASTICSEARCH_PORT = 9200
# ELASTICSEARCH_INDEX = 'meetups'
# ELASTICSEARCH_TYPE = 'meetup'
# ELASTICSEARCH_UNIQ_KEY = 'link'