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

    comment_content = request.POST.get('comments')
    user = BlogUser.objects.get(username=request.session['username'])
    post_slno = request.POST.get("post_slno")
    post = Post.objects.get(sl_no=post_slno)

    comment = BlogComment(comment=comment_content, user=user, post=post)
    comment.save()
    messages.success(request, "Your Comment has been Posted")

    return redirect(f'/blog/{post.slug}')
