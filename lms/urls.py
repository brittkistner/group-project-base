from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url("^$", TemplateView.as_view(template_name="index.html"), name="slides_home"),
    url("^test$", TemplateView.as_view(template_name="test.html"), name="test"),
    url('^get_slides/(?P<week_number>\w+)/(?P<day>\w+)/$',
        'slides.views.get_slides', name='get_slides'),
    url('^subset_comment/(?P<week_number>\w+)/(?P<day>\w+)/(?P<slide_set>\w+)/(?P<slide_number>\w+)$',
        'slides.views.subset_comment', name='update_comments'),
    url('^front_comment/(?P<week_number>\w+)/(?P<day>\w+)/(?P<slide_set>\w+)/$',
        'slides.views.front_comment', name='front_comment'),

    # LOGIN AND REGISTER
    url("^login/$", 'django.contrib.auth.views.login', name='login'),
    url("^register/$", 'slides.views.register', name="register"),
    url("^logout/$", 'django.contrib.auth.views.logout', name='logout'),


    # PASSWORD RESET
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'django.contrib.auth.views.password_reset_confirm',
    name='password_reset_confirm'),

    #PROFILE
    url(r'^profile/$', 'slides.views.profile', name='profile'),
    url(r'^profile/edit/$', 'slides.views.edit_profile', name='edit_profile'),

    # FETCH SLIDES & RESOURCES
    # url(r'^get_slides/(?P<week_number>\w+)/(?P<day>\w+)/$', 'slides.views.get_slides', name="get_slides"), #BK changed this
    url(r'^create_comment/(?P<week_number>\w+)/(?P<day>\w+)/(?P<slide_set>\d+)/(?P<slide_number>\d+)/$',
        'slides.views.create_comment', name='create_comment'),
    url(r'^create_comment/$', 'slides.views.create_comment', name='create_comment'),

    # Week 1 - OO Python
    url("^week1/1/$", TemplateView.as_view(template_name="week1/1.html"), name="week1_day1"),
    url("^week1/2/$", TemplateView.as_view(template_name="week1/2.html"), name="week1_day2"),
    url("^week1/3/$", TemplateView.as_view(template_name="week1/3.html"), name="week1_day3"),
    url("^week1/4_am/$", TemplateView.as_view(template_name="week1/4_am.html"), name="week1_day4_am"),
    url("^week1/4_pm/$", TemplateView.as_view(template_name="week1/4_pm.html"), name="week1_day4_pm"),

    # Week 2 - DB Intro + Introductory Django
    url("^week2/1_am/$", TemplateView.as_view(template_name="week2/1_am.html"), name="week2_day1_am"),
    url("^week2/1_pm/$", TemplateView.as_view(template_name="week2/1_pm.html"), name="week2_day1_pm"),
    url("^week2/2_am/$", TemplateView.as_view(template_name="week2/2_am.html"), name="week2_day2_am"),
    url("^week2/2_pm/$", TemplateView.as_view(template_name="week2/2_pm.html"), name="week2_day2_pm"),
    url("^week2/3_am/$", TemplateView.as_view(template_name="week2/3_am.html"), name="week2_day3_am"),
    url("^week2/3_pm/$", TemplateView.as_view(template_name="week2/3_pm.html"), name="week2_day3_pm"),
    url("^week2/4_am/$", TemplateView.as_view(template_name="week2/4_am.html"), name="week2_day4_am"),
    url("^week2/4_pm/$", TemplateView.as_view(template_name="week2/4_pm.html"), name="week2_day4_pm"),
    url("^week2/5_am/$", TemplateView.as_view(template_name="week2/5_am.html"), name="week2_day5_am"),
    url("^week2/5_pm/$", TemplateView.as_view(template_name="week2/5_pm.html"), name="week2_day5_pm"),

    # Start Project Cheatsheet
    url("^start_project_cheatsheet/$", TemplateView.as_view(template_name="start_project.html"), name="start_project"),

    # Week 3 - Introductory Django
    url("^week3/1_am/$", TemplateView.as_view(template_name="week3/1_am.html"), name="week3_day1_am"),
    url("^week3/1_pm/$", TemplateView.as_view(template_name="week3/1_pm.html"), name="week3_day1_pm"),
    url("^week3/2_am/$", TemplateView.as_view(template_name="week3/2_am.html"), name="week3_day2_am"),
    url("^week3/2_pm/$", TemplateView.as_view(template_name="week3/2_pm.html"), name="week3_day2_pm"),
    url("^week3/3_am/$", TemplateView.as_view(template_name="week3/3_am.html"), name="week3_day3_am"),
    url("^week3/3_pm/$", TemplateView.as_view(template_name="week3/3_pm.html"), name="week3_day3_pm"),
    url("^week3/lab/$", TemplateView.as_view(template_name="week3/lab.html"), name="week3_lab"),
)


