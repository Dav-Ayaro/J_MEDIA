from django.shortcuts import render, redirect
from django.contrib.auth import  login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import ReleaseForm
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.http import FileResponse
from django.shortcuts import get_object_or_404
import random, string
from urllib.parse import urlencode
from django.utils import timezone
from django.urls import reverse
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password

# Create your views here.

class SiteRequirements():
    def __init__(self):
        pass

    def random_func(self, length):
        return ''.join([random.choice(string.ascii_letters + string.digits) for i in range (length)])
    
    def Time(self):
        return timezone.datetime.now().date()
    
class RenderUrls(SiteRequirements):
    def render_view(self, request, view_file, **kwargs):
        return render(request, view_file, kwargs)

    def redirection_func(self, redirect_path=None, **kwargs):
        if kwargs:
            redirect_path += '?' + urlencode(kwargs)
        return HttpResponseRedirect(reverse(redirect_path))
    
object = RenderUrls()

def index_page(request):
    time = object.Time()
    Famous = Famous_Artist.objects.all()
    slides = Slide.objects.all()
    return object.render_view(request, view_file='jala_app/index.html',time=time, Famous=Famous, slides=slides)

def slideshow_view(request):
    slides = Slide.objects.all()
    return object.render_view(request, view_file='jala_app/slide.html', slides=slides)

def about_page(request):
    return object.render_view(request, view_file='jala_app/about.html')

def artist_page(request):
    artists = All_Artist.objects.all()
    return object.render_view(request, view_file='jala_app/artist.html', artists=artists)

def pricing_page(request):
    return object.render_view(request, view_file='jala_app/pricing.html')

def platform_page(request):
    return object.render_view(request, view_file='jala_app/platform.html')

def services_page(request):
    return object.render_view(request, view_file='jala_app/services.html')

def why_us_page(request):
    return object.render_view(request, view_file='jala_app/why_us.html')

def contact_us_page(request):
    return object.render_view(request, view_file='jala_app/contact.html')

def release_page(request):
    if request.method == "POST":
        capture_form_data = ReleaseForm(request.POST)
        if capture_form_data.is_valid():
            release = Release(
            ArtistName = capture_form_data.cleaned_data['ArtistName'],
            FeaturedArtist = capture_form_data.cleaned_data['FeaturedArtist'],
            SongWriters = capture_form_data.cleaned_data['SongWriters'],
            Producers = capture_form_data.cleaned_data['Producers'],
            ReleaseDate = capture_form_data.cleaned_data['ReleaseDate'],
            MusicType =  capture_form_data.cleaned_data['MusicType'],
            RadioChoices = capture_form_data.cleaned_data['RadioChoices'],
            GenderChoices = capture_form_data.cleaned_data['GenderChoices'],
            FileUpload = capture_form_data.cleaned_data['FileUpload'],
            CoverArt = capture_form_data.cleaned_data['CoverArt'],
            Muamala = capture_form_data.cleaned_data['Muamala'],
            PhoneNumber = capture_form_data.cleaned_data['PhoneNumber'],
            Email = capture_form_data.cleaned_data['Email'],
            )
            release.save()  # Save the object to the database
            try:
                #send mail block code
                subject = 'Submitted Successful'
                message = f"Dear {ArtistName}, \n\n Thank You for Submitting your file to us: \n\n  Here is your File information: \n\n Artist Name: {ArtistName}\n Featured Artist: {FeaturedArtist}\n Song Writters: {SongWriters}\n producers: {Producers}\n realease Date: {ReleaseDate}\n Music Type: {MusicType}\n In case of anthing kindly you can reach us out \n This is a secure place for your career\n Thank you fro choosing Jala Media entertainment."
                from_email = settings.DEFAULT_FROM_EMAIL
                recipient_list = [Email]
                send_mail(subject, message, from_email, recipient_list)
                return object.redirection_func(redirect_path = 'release_page')
            except (OSError, socket.gaierror):
                return object.render_view(request, view_file='jala_app/release.html', email_succesfully = True)
    return object.render_view(request, view_file='jala_app/release.html', capture_form_data=ReleaseForm())

