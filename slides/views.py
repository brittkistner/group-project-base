<<<<<<< HEAD
import json
from django.contrib.auth import authenticate, login
from django.contrib.comments import CommentForm
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from slides.forms import UserForm, CommmentForm
import uuid
from slides.models import Comment, Attachment

###############
# REGISTRATION #
###############
=======
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from slides.forms import UserForm

>>>>>>> 9c229482c3db6da2a0e64378b2eaa028acd67e3e

def register(request):
    if request.method == 'POST':
        print request.FILES
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
<<<<<<< HEAD
            return redirect("slides_home")
=======
            return redirect("/")
>>>>>>> 9c229482c3db6da2a0e64378b2eaa028acd67e3e

    else:
        form = UserForm()

    return render(request, "registration/register.html", {
        'form': form,
    })
<<<<<<< HEAD

###########
# PROFILE #
###########


def profile(request):
    return render(request, 'profile.html')

################
# EDIT PROFILE #
################


def edit_profile(request):
    if request.method == "POST":
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            if form.save():
                return redirect("profile")
    else:
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = UserForm(instance=request.user)
    data = {"form": form}
    return render(request, "edit_profile.html", data)



########################
# CREATING ATTACHMENTS #
#######################


def create_attachment(attachments, comment):
    attachments = []
    for attachment in attachments:
        unique_id = str(uuid.uuid4())
        while Attachment.objects.filter(uuid=unique_id).exists():
            unique_id = str(uuid.uuid4())
        attachment = Attachment.objects.create(file='', comment=comment, uuid=unique_id) #change file to attachment.file
        attachments.append(attachment)
    return attachments

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
def create_comment(request, week_number=3, day='2_am', slide_set=1, slide_number=1):
    # pass
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = json.loads(request.body)
            comment = Comment.objects.create(text=data['text'],
                                             user=request.user,
                                             week_number=week_number,
                                             day=day, slide_set=slide_set,
                                             slide_number=slide_number)

            #attachments come through as an array.
            attachments = create_attachment(data['attachments'], comment)

        #What should this response return.  Using HttpResponse for now
        response = serializers.serialize('json', [comment])
        return HttpResponse(response, content_type='application/json')
    else:
        form = CommmentForm()
    return render(request, "comment_form.html", {
        'form': form,
    })


#######################
# RETRIEVING COMMENTS #
######################
def get_comment(request, week_number, day, slide_set, slide_number):

    #will retrieve all comments for a specific week and (part) of day.  Does not separate based on slide number
    comments = Comment.objects.filter(week_number=week_number, day=day)

#######################
# REFRESH COMMENTS #
######################
def update_comments(request):
    pass
=======
>>>>>>> 9c229482c3db6da2a0e64378b2eaa028acd67e3e
