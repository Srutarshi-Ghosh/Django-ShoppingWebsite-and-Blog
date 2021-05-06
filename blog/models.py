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
    heading1 = models.CharField(max_length=500)
    content_head1 = models.CharField(max_length=5000)
    heading2 = models.CharField(max_length=500)
    content_head2 = models.CharField(max_length=5000)
    heading3 = models.CharField(max_length=500)
    content_head3 = models.CharField(max_length=5000)
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='blog/images', default='')

    def __str__(self):
        return self.title
