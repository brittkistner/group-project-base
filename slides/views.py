import code
import json
from django.contrib.auth import authenticate, login
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from slides.forms import UserForm, UpdateUserForm, CommentForm
import uuid
from slides.models import Comment, Attachment, Slide, User

###############
# REGISTRATION #
###############

def register(request):
    if request.method == 'POST':
        # print request.FILES
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # text_content = 'Thank you for signing up for our website, {}'.format(user.username)
            # html_content = '<h2>Thanks {} {} for signing up!</h2> <div>You joined at {}.  I hope you enjoy using our site</div>'.format(user.first_name, user.last_name, user.date_joined)
            # msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            login(request, new_user)
            return redirect("slides_home")

    else:
        form = UserForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

###########
# PROFILE #
###########
def profile(request):
    return render(request, 'profile.html')

################
# EDIT PROFILE #
################

def edit_profile(request):
    print request.user.name
    editable_userobject = User.objects.get(pk=request.user.id)
    if request.method == "POST":
        print "in post"
        form = UpdateUserForm(request.POST, request.FILES, instance=editable_userobject)
        if form.is_valid():
            print "VALID"
            # username = form.cleaned_data['username']
            # name = form.cleaned_data['name']
            editable_userobject.save()
            # User.objets.filter(pk=request.user.id).update(username=username, name=name)
        return redirect("profile")
    else:
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = UpdateUserForm(instance=request.user)
    data = {"user": request.user, "form": form}
    return render(request, "edit_profile.html", data)



######################
# CREATING COMMENTS #
#####################
# @csrf_exempt
# def create_comment(request, week_number, day, slide_set, slide_number, slide_header, url):
#     if request.method == 'POST':
#         print request.POST
#         print request.FILES
#         form = CommentForm(request.POST, request.FILES, week_number, day, slide_set, slide_number, slide_header, url)
#         if form.is_valid:
#         #validate that there is some text or an attachment
#             comment = form.save()
#             comment.user = request.user
#             comment.save()
#
#         response = serializers.serialize('json', [comment]) #ajax hide form and show resources pane
#         return HttpResponse(response, content_type='application/json')

@csrf_exempt
def create_comment(request, week_number, day, slide_set, slide_number):
    if request.method == 'POST':
        # data = json.loads(request.body)
        # print "This is data {}".format(data)
        files = json.loads(request.POST.getlist('files[]')[0])
        print files
        print request.POST.getlist('files[]')
        print request.POST.getlist('files[]')[0][0]
        print request.POST
        form = CommentForm(request.POST, week_number, day, slide_set, slide_number)
        if form.is_valid:
        #validate that there is some text or an attachment
            comment = form.save()
            comment.user = request.user
            comment.save()

        response = serializers.serialize('json', [comment]) #ajax hide form and show resources pane
        return HttpResponse(response, content_type='application/json')


#######################
# RETRIEVING COMMENTS #
######################
#Retrieve initial comments on slide load.  Once all comments are loaded, will continue to refresh comments section for the comment which is open.  See update_comments below.
#create ajax call

def get_slides(request, week_number, day):
    #will retrieve all comments for a specific week and (part) of day.  Does not separate based on slide number
    slides = Slide.objects.filter(
        day=day,
        week_number=week_number,
    ).order_by('id')
    return HttpResponse(serializers.serialize('json', slides), content_type='application/json')


#######################
# REFRESH COMMENTS #
######################
#Update comments for the comment section which is open (or which has just been clicked)
#create ajax call
def subset_comment(request, week_number, day, slide_set, slide_number):

    slides = Comment.objects.filter(
        slide__week_number=week_number,
        slide__day=day,
        slide__slide_set=slide_set,
        slide__slide_number=slide_number
    )

    return HttpResponse(serializers.serialize('json', slides), content_type='application/json')


def front_comment(request, week_number, day, slide_set):

    slides = Comment.objects.filter(
        week_number=week_number,
        day=day,
        slide_set=slide_set,
    )

    return HttpResponse(serializers.serialize('json', slides), content_type='application/json')
