from ..models import Blogpost, BlogComment, BlogUser
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages


def get_homepage(request):
    allPosts = Blogpost.objects.all()
    params = {'allPosts': allPosts}

    return render(request, 'bloghome.html', params)


def get_blogpost_page(request, slug):
    post = Blogpost.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    
    reply_dict = {}
    for reply in replies:
        if reply.parent.sl_no not in reply_dict:
            reply_dict[reply.parent.sl_no] = [reply]
        else:
            reply_dict[reply.parent.sl_no].append(reply)

    params = {'post': post, 'comments': comments, 'reply_dict': reply_dict}
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
    parent_sno = request.POST.get('parent_sno')
    
    if not parent_sno:
        comment = BlogComment(comment=comment_content, user=user, post=post)
    else:
        parent = BlogComment.objects.get(sl_no=parent_sno)
        comment = BlogComment(comment=comment_content, user=user, post=post, parent=parent)

    comment.save()
    messages.success(request, "Your Comment has been Posted")

    return redirect(f'/blog/{post.slug}')
