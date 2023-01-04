from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
        Post Model for Blog
    """

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    description = models.CharField(max_length=300, unique=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        """
            Metadata for Post Model
        """
        ordering = ['-created_on']

    def __str__(self):
        return self.title
