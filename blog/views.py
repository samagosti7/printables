from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import NewPostForm
from django.contrib import messages

# Create your views here.


@login_required()
def add_post(request):
    """
        Add Blog Post
    """
    if request.user.is_superuser:
        if request.method == "POST":
            form = NewPostForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Post submitted")
                return redirect(reverse("blog"))
            else:
                messages.error(
                    request, 'Form invalid')
        else:
            form = NewPostForm()
    else:
        messages.error(request, "You are not authorized to access that.")
        return redirect(reverse("blog"))

    context = {
        "form": form,
    }

    return render(request, 'blog/add_post.html', context)


@login_required()
def delete_post(request, post):
    """
        Delete Blog Post
    """
    if request.user.is_superuser:
        post = get_object_or_404(Post, slug=post)
        post.delete()
        messages.success(request, "Post deleted.")
        return redirect(reverse("blog"))
    else:
        messages.error(request, "You are not authorized to access that.")
        return redirect(reverse("blog"))
    
    


def blog(request):
    """
        Blog post list view
    """

    post_list = Post.objects.filter(status=1).order_by("-created_on")

    context = {
        "post_list": post_list
    }

    return render(request, "blog/blog.html", context)


def post_detail(request, post):
    """
        Blog post detail view
    """

    post = get_object_or_404(Post, slug=post)

    context = {
        "post": post
    }

    return render(request, "blog/post_detail.html", context)
