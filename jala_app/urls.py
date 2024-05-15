from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from .views import *

urlpatterns =[
    path('',index_page, name='index_page'),
    path('about', about_page, name='about_page'),
    path('why-us', why_us_page, name='why_us_page'),
    path('artist', artist_page, name='artist_page'),
    path('pricing', pricing_page, name='pricing_page'),
    path('platform', platform_page, name='platform_page'),
    path('our-service', services_page, name='services_page'),
    path('contact-us', contact_us_page, name='contact_us_page'),
    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)