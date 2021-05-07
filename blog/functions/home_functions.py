from ..models import Blogpost
from django.shortcuts import render


def get_homepage(request):
    params = parse_parameters(request)
    return render(request, 'bloghome.html', params)


def get_blogpost_page(request, slug):
    post = Blogpost.objects.filter(slug=slug).first()
    params = {'post': post}
    return render(request, 'blogpost.html', params)

def parse_parameters(request):
    allPosts = Blogpost.objects.all()
    params = {'allPosts': allPosts}
    return params