from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# https://docs.djangoproject.com/en/2.1/ref/models/fields/#model-field-types
# Field attributes on a model map to columns in a database table
class Post(models.Model):
    # title
    title = models.CharField(max_length=128)
    # text
    text = models.TextField(blank=True)
    # authur
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # created_date
    created_date = models.DateTimeField(auto_now_add=True)
    # modified_date
    modified_date = models.DateTimeField(auto_now=True)
    # published_date
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    # name
    name = models.CharField(max_length=128)
    # description
    description = models.TextField(blank=True)
    # posts
    # posts = Post.objects.get(title__contains=name)
    posts = models.ManyToManyField(Post, blank=True, related_name="categories")

    # this class is to prevent showing 'Categorys'
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
