from django import forms
from .models import Comment

CHOICES = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5')]
        
class PlaceChangeForm(forms.Form):
	    place_change = forms.CharField(label='Changes',widget=forms.Textarea)
	    # covid_rating = forms.CharField(widget=forms.Textarea)
	    covid_rating = forms.CharField(label='Covid_Rating',widget=forms.RadioSelect(choices=CHOICES))


class PlaceSubmitForm(forms.Form):
    place_change = forms.CharField(widget=forms.Textarea)
    covid_rating = forms.CharField(label='Covid_Rating',widget=forms.RadioSelect(choices=CHOICES))


class CommentForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea)
