from django.db import models
from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.conf import settings
from post.models import Post


class Project(models.Model):
    intro = models.CharField(max_length=50, null=False, validators=[MinLengthValidator(10)])
    thumbs = models.ImageField(blank=True, null=False, upload_to='thumbs/%y/%m/%d')
    capacity = models.PositiveSmallIntegerField(null=False, default=1,
                                                validators=[MinValueValidator(1), MaxValueValidator(30)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ManyToManyField(Post, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=False, related_name='members')
# Create your models here.


# Create your models here.
