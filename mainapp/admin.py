from django.contrib import admin
from .models import Place, Change, Leaderboard, Comment
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Place)
admin.site.register(Change)

@admin.register(Comment) #https://djangocentral.com/creating-comments-system-with-django/ -- referenced this tutorial for parts of the comments feature
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'body', 'change', 'created_on')
    search_fields = ('user_name', 'body')
    
admin.site.register(Leaderboard)
