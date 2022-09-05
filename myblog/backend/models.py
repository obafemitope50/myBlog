from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


STATUS = (
    (0, "Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    body = models.CharField(max_length=10000, unique=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default= 0)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    