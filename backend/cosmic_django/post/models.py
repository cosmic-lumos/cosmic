from django.db import models
from django.conf import settings
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="image/%Y/%m/%d", blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("post:post_detail", args=[self.pk])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)


class Comment(models.Model):
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, null=False, blank=False)
    text = models.TextField()

    def __str__(self):
        return self.text
# Create your models here.
