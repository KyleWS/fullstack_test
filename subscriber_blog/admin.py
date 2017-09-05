from django.contrib import admin
from .models import Subscriber, Post, Image
# Register your models here.

admin.site.register(Subscriber)
admin.site.register(Post)
admin.site.register(Image)
