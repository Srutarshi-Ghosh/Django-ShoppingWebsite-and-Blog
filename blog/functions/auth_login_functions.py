from ..models import BlogUser
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse

def loginUtil(request):
    
    if request.method != "POST":
        return HttpResponse("Page Not Accessable")

    login_username = request.POST['loginusername']
    login_password = request.POST['loginpassword']
    hashed_password = make_password(login_password)

    user = BlogUser.objects.filter(username=login_username).first()

    if user and check_password(login_password, user.password):
        messages.success(request, "Successfully logged in")
        request.session['username'] = login_username
        request.session['is_authenticated'] = True
        return redirect("/blog")

    messages.error(request, "Invalid credentials! Please try again")
    return redirect("/blog")
   

def logoutUtil(request):
    request.session['username'] = None
    request.session['is_authenticated'] = False
    messages.success(request, "Successfully logged out")
    return redirect("/blog")