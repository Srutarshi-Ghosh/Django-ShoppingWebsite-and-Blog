from django.shortcuts import render
from .models import Blogpost, Contact
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    myposts = Blogpost.objects.all()
    return render(request, 'bloghome.html', {'myposts': myposts})

def blogpost(request, slug):
    post = Blogpost.objects.filter(slug=slug).first()
    return render(request, 'blogpost.html', {'post': post})

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