from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="blogHome"),
    path('contact', views.contact, name="blogContact"),
    path('about', views.about, name="blogAbout"),
    path('<str:slug>', views.blogpost, name="blogHome"),
]
