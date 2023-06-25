from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="comment_likes", blank=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.content} by {self.name}"

    def number_of_likes(self):
        return self.likes.count()


class Club(models.Model):
    club_name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    club_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='club')
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['created_on']


