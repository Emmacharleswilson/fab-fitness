from django.contrib import admin
from .models import BlogPost, BlogComment


class BlogAdmin(admin.ModelAdmin):
    list_display = (
            "blog_title",
            "author",
            "blog_content",
    )


class BlogCommentAdmin(admin.ModelAdmin):
    """ Creates the admin interface for Blog Comment """

    list_display = (
        'comment_title',
        'comment',
        'blogpost',
        'comment_user'
    )


admin.site.register(BlogPost)
admin.site.register(BlogComment, BlogCommentAdmin)