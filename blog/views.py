from django.shortcuts import render
from blog.templatetags import extras

from .functions.auth_signup_functions import *
from .functions.auth_login_functions import *
from .functions.contact_functions import *
from .functions.blogpage_functions import *
from .functions.search_functions import *


def index(request):
    return get_homepage(request)


def blogpost(request, slug):
    return get_blogpost_page(request, slug)


def postComment(request):
    return postCommentsUtil(request)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return contactUtil(request)


def search(request):
    return searchUtil(request)


def handleSignUp(request):
    return signupUtil(request)
    

def handleLogin(request):
    return loginUtil(request)


def handleLogout(request):
    return logoutUtil(request)
