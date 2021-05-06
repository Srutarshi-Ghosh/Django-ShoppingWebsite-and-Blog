from django.db import models


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
