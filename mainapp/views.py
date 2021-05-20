from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from .models import Place, Change, Comment, Leaderboard
from .forms import PlaceChangeForm, PlaceSubmitForm, CommentForm
from django.contrib.auth.models import User
from django.db.models.query_utils import DeferredAttribute

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

class MapView(TemplateView):
    template_name = "mainapp/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['places_list'] = [
            {
                'place_id': p.id,
                'google_place_id': p.google_place_id,
                'place_name': p.place_name,
                'place_address': p.place_address,
                'place_changes': p.change_set.all()
            }
            for p in Place.objects.all()
        ]
        return context

    # def map(request):
    #     places_list = Place.objects.all()
    #     return render(request, 'mainapp/map.html', context={'places_list': places_list})

def places(request):
    places_list = Place.objects.all()
    context = {
        'places_list': places_list,
    }
    return render(request, 'mainapp/places.html', context)

def changes_details(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    return render(request, 'mainapp/changes.html', {'place': place})

def leaderboard(request):
    user_rankings = Leaderboard.objects.all().order_by('-num_submissions')
    return render(request, 'mainapp/leaderboard.html', {'leaderboard': user_rankings})

@login_required(login_url='/')
def submit_change(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    if request.method == 'POST':
        form = PlaceChangeForm(request.POST)

        if form.is_valid():
            place.change_set.create(place_change=form.cleaned_data['place_change'],
            covid_rating=form.cleaned_data['covid_rating'], submitting_user=request.user.get_username().title())
            #Update Leaderboard
            username = request.user.get_username().title() #https://stackoverflow.com/questions/12381756/django-calling-update-on-a-single-model-instance-retrieved-by-get - was helpful in finding the username and number of submissions for each Leaderboard object/user. (StackOverflow) 
            contained = Leaderboard.objects.filter(user = username)
            starting_submission = 1 
            if not contained: #https://stackoverflow.com/questions/1387727/checking-for-empty-queryset-in-django - used to check whether a Leaderboard instance already exists on our application, or if a new object must be created. (StackOverflow)
                l = Leaderboard.objects.create(user = username, num_submissions = starting_submission)
                l.save()
            else:
                l = Leaderboard.objects.get(user = username)
                l.num_submissions = l.num_submissions + 1
                l.save()
            return HttpResponseRedirect('/mainapp/map/places/'+str(place_id))
    else:
        form = PlaceChangeForm()

    return render(request, 'mainapp/submit_change.html', {'form': form})

@login_required(login_url='/')
def submit_place(request, google_id, street, name):
    if request.method == 'POST':
        form = PlaceSubmitForm(request.POST)

        if form.is_valid():
            if street == "undefined":
                street = "-"
            p = Place(place_name=name,
            place_address=street, 
            google_place_id=google_id)
            p.save()
            p.change_set.create(place_change=form.cleaned_data['place_change'],
            covid_rating=form.cleaned_data['covid_rating'], submitting_user=request.user.get_username().title())
            #Update Leaderboard
            username = request.user.get_username().title() 
            #print(username)
            contained = Leaderboard.objects.filter(user = username)
            starting_submission = 1 
            if not contained:
                l = Leaderboard.objects.create(user = username, num_submissions = starting_submission)
                l.save()
            else:
                l = Leaderboard.objects.get(user = username)
                l.num_submissions = l.num_submissions + 1
                l.save()
            return HttpResponseRedirect('/mainapp/map/places')
    else:
        form = PlaceSubmitForm()

    return render(request, 'mainapp/submit_place.html', {'form': form})

def comments_details(request, change_id):
    comments_list = Comment.objects.all()
    change = get_object_or_404(Change, pk=change_id)
    return render(request, 'mainapp/comments.html', {'change': change, 'comments_list':comments_list})

@login_required(login_url='/')
def submit_comment(request, change_id):
    change = get_object_or_404(Change, pk=change_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            change.comment_set.create(body = form.cleaned_data['body'], user_name = request.user.get_username().title())
            return HttpResponseRedirect('/mainapp/map/places/'+str(change_id)+'/comments')
    else:
        form = CommentForm()

    return render(request, 'mainapp/submit_comments.html', {'form': form})