from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import NewPostForm
from django.contrib import messages

# Create your views here.


@login_required
def delete_post(request, Post):
    """
        Delete Blog Post
    """
    if not request.user.is_superuser:
        messages.error(request, "You are not authorized to perform that action.")
        return redirect(reverse("blog"))

        post = get_object_or_404(Post, slug=post)
        post.delete()
        messages.success("Post deleted.")


@login_required
def delete_post(request, Post):
    """
        Delete Blog Post
    """
    if not request.user.is_superuser:
        messages.error(request, "You are not authorized to perform that action.")
        return redirect(reverse("blog"))

        post = get_object_or_404(Post, slug=post)
        post.delete()
        messages.success("Post deleted.")



