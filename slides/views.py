import json
import urllib2
from bs4 import BeautifulSoup
from django.contrib.auth import authenticate, login
from django.contrib.comments import CommentForm
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from slides.forms import UserForm, CommmentForm, NotesSearchForm
import uuid
from slides.models import Comment, Attachment, Slide, RuPageModel

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
    if request.method == "POST":
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        # pass in request.files
        # User.objets.filter(pk=request.user.id).update(pass in all fields, field=???)
        form = UserForm(request.POST, request.FILES, instance=request.user)
        user = form.save(commit=False)
        user.save()
        return redirect("profile")
    else:
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = UserForm(instance=request.user)
    data = {"user": request.user, "form": form}
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
#Retrieve initial comments on slide load.  Once all comments are loaded, will continue to refresh comments section for the comment which is open.  See update_comments below.
#create ajax call
def get_comment(request, week_number, day):
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


def root(request):
    """
    Search > Root
    """

    # we retrieve the query to display it in the template
    form = NotesSearchForm(request.GET)

    # we call the search method from the NotesSearchForm. Haystack do the work!
    results = form.search()

    return render(request, 'search/search_root.html', {
        'search_query' : "New York",
        'notes' : results,
    })

def search(request):
    """
    Search > Root
    """

    # we retrieve the query to display it in the template
    form = NotesSearchForm(request.GET)

    # we call the search method from the NotesSearchForm. Haystack do the work!
    results = form.search()

    return render(request, 'search/search_root.html', {
        'search_query' : "New York",
        'notes' : results,
    })



def parse(request):
    start_urls = [
    "http://127.0.0.1:8000/week1/1/",
    # "http://127.0.0.1:8000/week1/2/",
    # "http://127.0.0.1:8000/week1/3/",
    # "http://127.0.0.1:8000/week1/4_am/",
    ]
    for cururl in start_urls:
        filename = cururl.split("/")
        file = filename[3]+filename[4]
        source = urllib2.urlopen(cururl).read()
        soup = BeautifulSoup(source)
        body = soup.find('div',id='classSlides')
        sections = body.find_all('section', recursive=0)
        page_number = 1
        page_down = 0
        for section in sections:
            sub = section.find_all('section', recursive=0)
            for each in sub:
                url = cururl+'#'+'/'+ str(page_number) + '/' + str(page_down)
                text = str(each)
                print url,'url'
                print page_down,'down'
                print page_number,'number'
                print each
                # item = RuPageModel(text=text, page_url=url, page_number=page_number, page_down=page_down)
                # item.save()
                page_down+=1

            if len(sub)==0:
                url = cururl+'#'+'/'+ str(page_number) + '/' + str(page_down)
                text = str(section)
                print page_down,'down'
                print page_number,'number'
                print section,'single page'
                # item = RuPageModel(text=text, page_url=url, page_number=page_number, page_down=page_down)
                # item.save()

            page_number+=1
            page_down = 0

from django.shortcuts import render_to_response
from .forms import NotesSearchForm, RuPageModelSearchForm

def notes(request):
    form = NotesSearchForm(request.GET)
    notes = form.search()
    return render_to_response('notes.html', {'notes': notes})

def rusearch(request):
    form = RuPageModelSearchForm(request.GET)
    pages = form.search()
    return render_to_response('rusearch.html', {'pages': pages})


# from haystack.query import SearchQuerySet
# all_results = SearchQuerySet().all()
# hello_results = SearchQuerySet().filter(content='hello')
# hello_world_results = SearchQuerySet().filter(content='hello world')
# unfriendly_results = SearchQuerySet().exclude(content='hello').filter(content='world')
# recent_results = SearchQuerySet().order_by('-pub_date')[:5]
#
# # Using the new input types...
# from haystack.inputs import AutoQuery, Exact, Clean
# sqs = SearchQuerySet().filter(content=AutoQuery(request.GET['q']), product_type=Exact('ancient book'))
#
# if request.GET['product_url']:
#     sqs = sqs.filter(product_url=Clean(request.GET['product_url']))

