from ..models import Blogpost, BlogComment, BlogUser
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages


def get_homepage(request):
    allPosts = Blogpost.objects.all()
    params = {'allPosts': allPosts}

    return render(request, 'bloghome.html', params)


def get_blogpost_page(request, slug):
    post = Blogpost.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post)

    params = {'post': post, 'comments': comments}

    return render(request, 'blogpost.html', params)


def postCommentsUtil(request):
    if request.method != 'POST':
        return HttpResponse("<h1>Not Allowed</h1>")

    post_id = request.POST.get("post_id")
    post = Blogpost.objects.get(post_id=post_id)

    if not request.session['is_authenticated']:
        messages.error(request, "You need to be Logged in to Post a Comment")
        return redirect(f'/blog/{post.slug}')

    comment_content = request.POST.get('comment')
    user = BlogUser.objects.get(username=request.session['username'])
    

    comment = BlogComment(comment=comment_content, user=user, post=post)
    comment.save()
    messages.success(request, "Your Comment has been Posted")

    return redirect(f'/blog/{post.slug}')
