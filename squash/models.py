from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    email = models.EmailField()
    updated_on = models.DateTimeField(auto_now=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="comment_likes", blank=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def number_of_likes(self):
        return self.likes.count()


