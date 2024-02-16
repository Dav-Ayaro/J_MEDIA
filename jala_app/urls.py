from django.urls import path

from .views import *

urlpatterns =[
    path('',index_page, name='index_page'),
    path('about', about_page, name='about_page'),
    path('artist', artist_page, name='artist_page'),
    path('pricing', pricing_page, name='pricing_page'),
    path('platform', platform_page, name='platform_page'),
]