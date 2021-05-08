from django.shortcuts import render
from .functions.auth_signup_functions import *
from .functions.auth_login_functions import *
from .functions.contact_functions import *
from .functions.home_functions import *
from .functions.search_functions import *


def index(request):
    return get_homepage(request)


def blogpost(request, slug):
    return get_blogpost_page(request, slug)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return parse_contact(request)


def search(request):
    return searchUtil(request)


def handleSignUp(request):
    return signup(request)
    

def handleLogin(request):
    return login(request)


def handleLogout(request):
    return logout(request)
