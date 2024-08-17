from django.contrib import admin
from .models import Post, Comment, Action, Contact
# Register your models here.


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Action)
admin.site.register(Contact)