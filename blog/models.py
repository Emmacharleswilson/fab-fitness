from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    """ Create blogpost in database """

    author = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    blog_title = models.CharField(
        max_length=60, null=True, blank=False)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True)
    blog_body = models.TextField()
    image = models.ImageField(
        null=True, blank=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.blog_title


class BlogComment(models.Model):
    """ Create blog comments in database """

    blogpost = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE)
    comment_user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True)
    comment_title = models.CharField(
        max_length=50, null=False, blank=False)
    comment = models.TextField(
        max_length=2048, null=False, blank=False)

    def __str__(self):
        return self.comment_title
