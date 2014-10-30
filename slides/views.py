import json
from django.contrib.auth import authenticate, login
from django.contrib.comments import CommentForm
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from slides.forms import UserForm, CommmentForm, UpdateUserForm
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



########################
# CREATING ATTACHMENTS #
#######################

# def create_attachment(attachments, comment):
#     attachments = []
#     for attachment in attachments:
#         unique_id = str(uuid.uuid4())
#         while Attachment.objects.filter(uuid=unique_id).exists():
#             unique_id = str(uuid.uuid4())
#         attachment = Attachment.objects.create(file='', comment=comment, uuid=unique_id) #change file to attachment.file
#         attachments.append(attachment)
#     return attachments

###################
# RESOURCE UPLOAD #
###################

# def image_upload(request):
#     response = {'files': []}
#     # Loop through our files in the files list uploaded
#     file_info = {}
#     for file in request.FILES.getlist('files[]'):
#         file_info[file.name] = file
#
#         # Save output for return as JSON
#         response['files'].append({
#             'name': '%s' % file.name,
#             'size': '%d' % file.size,
#             # 'thumbnailUrl': '%s' % new_image.picture.url,
#             # 'deleteUrl': '\/image\/delete\/%s' % file.name,
#             # "deleteType": 'DELETE'
#         })
#
#     return HttpResponse(json.dumps(response), content_type='application/json')

######################
# CREATING COMMENTS #
#####################
@csrf_exempt
def create_comment(request, week_number, day, slide_set, slide_number):
    # pass
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, week_number, day, slide_set, slide_number)
        if form.is_valid:
        #validate that there is some text or an attachment
            comment = form.save() #return the comment

        #What should this response return.  Using HttpResponse for now
        response = serializers.serialize('json', [comment])
        return HttpResponse(response, content_type='application/json')
    return render(request, "comment_form.html", {
        'form': form,
    })


#######################
# RETRIEVING COMMENTS #
######################
#Retrieve initial comments on slide load.  Once all comments are loaded, will continue to refresh comments section for the comment which is open.  See update_comments below.
#create ajax call
def get_slides(request, week_number, day):
    #will retrieve all comments for a specific week and (part) of day.  Does not separate based on slide number
    slides = Slide.objects.filter(week_number=week_number, day=day).order_by('slide_set','slide_number', 'date')
    data = {'slides': slides}
    return render(request, "all_slides.html", data)

#######################
# REFRESH COMMENTS #
######################
#Update comments for the comment section which is open (or which has just been clicked)
#create ajax call
def update_comments(request, week_number, day, slide_set, slide_number):
    comments = Comment.objects.filter(week_number=week_number, day=day, slide_set=slide_set, slide_number=slide_number).order_by('date')
    data = {'comments': comments}
    return render(request, "update_comments.html", data)





# def test_comment(request):
#     return render(request, "test_comment.html")

