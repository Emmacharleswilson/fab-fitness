from django import forms
from .widgets import CustomClearableFileInput
from .models import BlogPost, BlogComment


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = (
            'blog_title',
            'blog_body',
            'image',
            )

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = (
            'comment_title',
            'comment'
            )
