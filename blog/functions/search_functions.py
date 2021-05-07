from django.shortcuts import render
from ..models import Blogpost



def searchUtil(request):
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
