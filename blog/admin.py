from django.contrib import admin
from .models import Blogpost, Contact, BlogUser, BlogComment

admin.site.register((Blogpost, BlogComment))
admin.site.register(Contact)
admin.site.register(BlogUser)
