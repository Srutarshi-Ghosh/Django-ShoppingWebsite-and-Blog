from django.db import models
from django.utils.timezone import now


class Contact(models.Model):
    sl_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Messaage from ' + self.name + ' - ' + self.email



class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    content = models.TextField(default='')
    author = models.CharField(max_length=50, default='')
    slug = models.CharField(max_length=130, default='')
    pub_date = models.DateField(blank=True)
    thumbnail = models.ImageField(upload_to='blog/images', default='')

    def __str__(self):
        return self.title + ' by ' + self.author


class BlogUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=500)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' (' + self.username + ')'

    
class BlogComment(models.Model):
    sl_no = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[:13] + '... by ' + self.user.username

