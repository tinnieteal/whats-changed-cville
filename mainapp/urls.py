from django.urls import path, re_path

from . import views
from .views import MapView

app_name = 'mainapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('map/', MapView.as_view(), name='map'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('map/places/', views.places, name='places'),
    re_path(r'^map/places/submit_place/(?P<google_id>.+)&(?P<street>.+)&(?P<name>.+)/', views.submit_place, name='submit_place'),
    path('map/places/<int:place_id>/', views.changes_details, name='changes'),
    path('map/places/<int:place_id>/submit_change', views.submit_change, name='submit_change'),
    path('map/places/<int:change_id>/submit_comment/', views.submit_comment, name='submit_comments'),
    path('map/places/<int:change_id>/comments/', views.comments_details, name = 'comments')
]
