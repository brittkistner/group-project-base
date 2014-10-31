import code
import json
import urllib2
from bs4 import BeautifulSoup
from django.contrib.auth import authenticate, login
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from slides.forms import UserForm, UpdateUserForm, CommentForm
import uuid
from slides.models import Comment, Attachment, Slide, User
from slides.models import Comment, Attachment, Slide, RuPageModel
from django.shortcuts import render_to_response
from .forms import NotesSearchForm, RuPageModelSearchForm
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

def get_slides(request, week_number, day, slide_set):
    #will retrieve all comments for a specific week and (part) of day.  Does not separate based on slide number
    slides = Comment.objects.filter(
        slide__week_number=week_number,
        slide__day=day,
        slide_set=slide_set
    )
    return HttpResponse(serializers.serialize('json', slides), content_type='application/json')

#######################
# REFRESH COMMENTS #
######################
#Update comments for the comment section which is open (or which has just been clicked)
#create ajax call
def update_comments(request, day, slide_set):
    slides_and_comments = []
    slides = Comment.objects.filter(slide__day=day, slide__slide_set=slide_set)
    # for slide in slides:
    #     for comment in slide.comments.all():
    #         slides_and_comments.append(list(slide) + list(comment.text))


    return HttpResponse(serializers.serialize('json', slides), content_type='application/json')





# def test_comment(request):
#     return render(request, "test_comment.html")


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
    "http://127.0.0.1:8000/week1/2/",
    "http://127.0.0.1:8000/week1/3/",
    "http://127.0.0.1:8000/week1/4_am/",
    "http://127.0.0.1:8000/week1/4_am/",
    "http://127.0.0.1:8000/week1/4_pm/",
    "http://127.0.0.1:8000/week2/1_am/",
    "http://127.0.0.1:8000/week2/1_pm/",
    "http://127.0.0.1:8000/week2/2_am/",
    "http://127.0.0.1:8000/week2/2_pm/",
    "http://127.0.0.1:8000/week2/3_am/",
    "http://127.0.0.1:8000/week2/3_pm/",
    "http://127.0.0.1:8000/week2/4_am/",
    "http://127.0.0.1:8000/week2/4_pm/",
    "http://127.0.0.1:8000/week2/5_am/",
    "http://127.0.0.1:8000/week2/5_pm/",
    "http://127.0.0.1:8000/week3/1_am/",
    "http://127.0.0.1:8000/week3/1_pm/",
    "http://127.0.0.1:8000/week3/2_am/",
    "http://127.0.0.1:8000/week3/2_pm/",
    "http://127.0.0.1:8000/week3/3_am/",
    "http://127.0.0.1:8000/week3/3_pm/",
    "http://127.0.0.1:8000/week3/lab/",

    ]
    print 'running'
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
                item = RuPageModel(text=text, page_url=url, page_number=page_number, page_down=page_down)
                item.save()
                page_down+=1

            if len(sub)==0:
                url = cururl+'#'+'/'+ str(page_number) + '/' + str(page_down)
                text = str(section)
                print page_down,'down'
                print page_number,'number'
                print section,'single page'
                item = RuPageModel(text=text, page_url=url, page_number=page_number, page_down=page_down)
                item.save()

            page_number+=1
            page_down = 0



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

