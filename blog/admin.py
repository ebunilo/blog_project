from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Tag, Post
from .models import User

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("slug", "published_at")

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(User, UserAdmin)
