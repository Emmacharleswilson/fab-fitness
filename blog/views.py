from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import BlogPost, BlogComment
from .forms import BlogForm, CommentForm


def blog(request):
    """ A view to show blog posts details """
    # Fetches all blogposts from database
    blogposts = BlogPost.objects.all()

    context = {
        'blogposts': blogposts,
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, blogpost_id):
    """ A view to display blog detail page"""
    # Fetches specific blopost and blog comment from database
    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    blogcomments = BlogComment.objects.filter(blogpost=blogpost)

    context = {
        'blogpost': blogpost,
        'blogcomments': blogcomments,
    }

    return render(request, 'blog/blog-detail.html', context)


@login_required
def add_blogpost(request):
    """ Adds a blogpost to the blog section """

    if not request.user.is_authenticated:
        messages.error(
            request, 'Sorry, you can only add a \
                blog post if you are a registered user!')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            # Saves blogpost to database
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            messages.info(
                request, 'New blogpost added')
            return redirect(reverse('blog'))
        else:
            messages.error(
                request,
                'Failed to add blogpost 😔 Please check the form is valid.')
    else:
        form = BlogForm()

    form = BlogForm()
    template = 'blog/add-blogpost.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_blogpost(request, blogpost_id):
    """ Deletes blog post from blog section"""

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)

    if request.user == blogpost.author or request.user.is_superuser:
        # Removes blopost from database
        blogpost.delete()
        messages.info(request, "Blogpost succesfully deleted")
        return redirect(reverse('blog'))
    else:
        messages.error(
            request, "Sorry, you didn't create \
                this blogpost so you can't delete it")
        return redirect(reverse('blog'))


@login_required
def edit_blogpost(request, blogpost_id):
    """ Edits blog post from blog section"""

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)

    if request.user == blogpost.author or request.user.is_superuser:
        # Updates blogpost in database
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES, instance=blogpost)
            if form.is_valid():
                form.save()
                messages.info(request, 'Successfully updated blog post!')
                return redirect(reverse('blog_detail', args=[blogpost.id]))
            else:
                messages.error(
                        request, 'Failed to update the blog post. \
                            Please make sure form is valid')
        else:
            form = BlogForm(instance=blogpost)
    else:
        messages.error(
                request, 'Sorry, you didnt create this \
                    blogpost so you cant edit it')
        return redirect(reverse('home'))

    template = 'blog/edit-blogpost.html'
    context = {
        'form': form,
        'blogpost': blogpost,
    }

    return render(request, template, context)


@login_required
def add_blogcomment(request, blogpost_id):
    """ Adds comment and attaches to blogpost """

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Saves blog comment to database
            blogcomment = form.save(commit=False)
            blogcomment.comment_user = request.user
            blogcomment.blogpost = blogpost
            blogcomment.save()
            messages.info(
                request, f'Thanks for your \
                    commenting on {blogpost.blog_title}')
            return redirect(reverse('blog_detail', args=[blogpost.id]))
        else:
            messages.error(request,
                           'Sorry something went wrong 😔 Please try again')
    else:
        form = CommentForm(instance=blogpost)
    template = 'blog/add-blogcomment.html'
    context = {
        'form': form,
        'blogpost': blogpost,
    }

    return render(request, template, context)


@login_required
def delete_blogcomment(request, blogcomment_id):
    """ Deletes comment from blogpost """

    blogcomment = get_object_or_404(BlogComment, pk=blogcomment_id)

    if request.user == blogcomment.comment_user or request.user.is_superuser:
        # Removes blog comment from database
        blogcomment.delete()
        messages.info(request, "Comment succesfully deleted")
        return redirect(reverse('blog'))
    else:
        messages.error(request, "Sorry, this isn't your comment to delete")
        return redirect(reverse('blog'))


@login_required
def edit_blogcomment(request, blogcomment_id):
    """ Edits blog comment on blogpost """

    blogcomment = get_object_or_404(BlogComment, pk=blogcomment_id)
    blogpost = get_object_or_404(BlogPost, pk=blogcomment.blogpost.id)

    if request.user == blogcomment.comment_user or request.user.is_superuser:
        # Updates blogcomment in database
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=blogcomment)
            if form.is_valid():
                form.save()
                messages.info(
                    request, 'Successfully updated comment!')
                return redirect(reverse('blog_detail', args=[blogpost.id]))
            else:
                messages.error(
                        request, 'Failed to update the blog comment. \
                            Please make sure form is valid')
        else:
            form = CommentForm(instance=blogcomment)
    else:
        messages.error(
                        request,
                        'Not your blog comment to edit')
        return redirect(reverse('blog'))

    template = 'blog/edit-blogcomment.html'
    context = {
        'form': form,
        'blogpost': blogpost,
        'blogcomment': blogcomment,
    }

    return render(request, template, context)
