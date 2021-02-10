from django.contrib import admin
from .models import Tag, Publication, Comment
# Register your models here.

admin.site.register(Publication)
admin.site.register(Tag)
admin.site.register(Comment)
