from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings

class Tag(models.Model):
    value = models.CharField(max_length=100)

    def __str__(self):
        return str(self.value)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    summary = models.TextField(max_length=500)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")

    def __str__(self):
        return str(self.title)


class User(AbstractUser):
    pass
