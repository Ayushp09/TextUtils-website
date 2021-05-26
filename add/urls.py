from os import name
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns =[
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('analyze', views.analyze, name='analyze'),
    path('contact',views.contact, name='contact')
]
