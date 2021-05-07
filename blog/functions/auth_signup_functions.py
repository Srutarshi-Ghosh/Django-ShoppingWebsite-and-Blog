from django.shortcuts import render, HttpResponse, redirect
from ..models import BlogUser
from django.contrib.auth.hashers import make_password
from django.contrib import messages




def signup(request):
    if request.method != 'POST':
        return HttpResponse("<h1>Not Allowed</h1>")
    
    username = request.POST['username']
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    email = request.POST['email']
    pass1 = request.POST['pass1']
    pass2 = request.POST['pass2']

    auth_success, auth_message = authenticate_signup(username, first_name, last_name, pass1, pass2)
    if not auth_success:
        messages.error(request, auth_message)
        return redirect('/blog')
    
    password = make_password(pass1)
    myuser = BlogUser(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
    myuser.save()
    messages.success(request, "Your account has been successfully created")
    return redirect('/blog')



def authenticate_signup(username, first_name, last_name, pass1, pass2):

    username_auth, message = authenticate_username(username)
    if not username_auth:
        return False, message

    first_name_auth, message = authenticate_firstname(first_name) 
    if not first_name_auth:
        return False, message

    last_name_auth, message = authenticate_lastname(first_name) 
    if not last_name_auth:
        return False, message
    
    password_auth, message = authenticate_password(pass1, pass2)
    if not password_auth:
        return False, message

    return True, "Success"



def authenticate_username(username):
    if len(username) > 20:
        return False, "Username cannot be more then 20 characters"

    if len(username) < 2:
        return False, "Username should be atleast 2 characters"

    if not username.isalnum():
        return False, "Username can only contain letters and numbers"

    if BlogUser.objects.filter(username=username).count():
        return False, "This username already Exists. Choose another username"

    return True, "Success"


def authenticate_firstname(first_name):
    if not first_name.isalpha():
        return False, "First Name can only contain letters"
    return True, "Success"


def authenticate_lastname(first_name):
    if not first_name.isalpha():
        return False, "First Name can only contain letters"
    return True, "Success"


def authenticate_password(pass1, pass2):
    if pass1 != pass2:
        return False, "Your Passwords do not match"

    password = pass1

    if len(password) < 5:
        return False, "Your password is too weak. Try a Stronger Password"

    return True, "Success"
    
   




