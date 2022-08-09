from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path(
        'add-blogpost/', views.add_blogpost, name='add_blogpost'),
    path(
        '<int:blogpost_id>/', views.blog_detail, name='blog_detail'),
    path(
        'delete-blogpost/<int:blogpost_id>/',
        views.delete_blogpost, name='delete_blogpost'),
    path(
        'edit-blogpost/<int:blogpost_id>/',
        views.edit_blogpost, name='edit_blogpost'),
    path(
        'add-blogcomment/<int:blogpost_id>/',
        views.add_blogcomment, name='add_blogcomment'),
    path(
        'delete-blogcomment/<int:blogcomment_id>/',
        views.delete_blogcomment, name='delete_blogcomment'),
    path(
        'edit-blogcomment/<int:blogcomment_id>/',
        views.edit_blogcomment, name='edit_blogcomment'),
]
