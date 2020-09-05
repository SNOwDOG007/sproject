from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
# DJANGO-ORM (Object relational mapping)

#BLOG
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    count = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255, null=True)
    # category = models.ManyToManyField(Category, related_name="news_categoreis")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to="blog", null=True)

