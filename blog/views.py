from django.shortcuts import render, HttpResponse, redirect
from .models import Blogpost, Contact, BlogUser
from django.contrib import messages
from .functions.auth_signup_functions import *
from .functions.auth_login_functions import *


def index(request):
    allPosts = Blogpost.objects.all()
    params = {'allPosts': allPosts}
    return render(request, 'bloghome.html', params)

def blogpost(request, slug):
    post = Blogpost.objects.filter(slug=slug).first()
    params = {'post': post}
    return render(request, 'blogpost.html', params)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')

        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")
        else: 
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your form has been submitted")
    return render(request, 'contact.html')


def search(request):
    query = request.GET['query']

    if len(query) > 70:
        posts = Blogpost.objects.none()
    else:
        title_matched_posts = Blogpost.objects.filter(title__icontains=query)
        content_matched_posts = Blogpost.objects.filter(content__icontains=query)
        posts = title_matched_posts.union(content_matched_posts)

    if posts.count() == 0:
        messages.warning(request, "No search results found. Please refine your Query!")
    params = {'posts': posts, 'query': query}
    return render(request, 'search.html', params)


def handleSignUp(request):
    return signup(request)
    

def handleLogin(request):
    return login(request)


def handleLogout(request):
    return logout(request)