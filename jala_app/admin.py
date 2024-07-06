from django.contrib import admin
from .models import *

# Register your models here.

class UserView(admin.ModelAdmin):
    list_display = ['pk','username', 'email', 'is_superuser', 'password']

class Famous_ArtistView(admin.ModelAdmin):
    list_display = ['adminId', 'artistName', 'description', 'artistPhoto', 'uploadDate', 'slug']
    # prepopulated_fields = {'slug': ('updateTitle', 'date') }
    # search_fields = ('updateTitle', 'slug')

class All_ArtistView(admin.ModelAdmin):
    list_display = ['adminId', 'artistName', 'artistPhoto', 'uploadDate']

class Slide_view(admin.ModelAdmin):
    list_display = ['image','link','caption']


admin.site.register(UserAccounts, UserView),
admin.site.register(Famous_Artist, Famous_ArtistView),
admin.site.register(All_Artist, All_ArtistView),
admin.site.register(Slide,Slide_view),