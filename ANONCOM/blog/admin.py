from django.contrib import admin
from .models import Post, Comments, Post_anon, AnonComments

admin.site.register(Post)
admin.site.register(Comments)

admin.site.register(AnonComments)
admin.site.register(Post_anon)

