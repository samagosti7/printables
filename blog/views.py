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
    if not request.user.is_superuser:
        messages.error(request, "You are not authorized to perform that action.")
        return redirect(reverse("blog"))

        if request.method == "POST":
            form = NewPostForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Post submitted")
                return redirect(reverse("blog"))
        else:
            form = NewPostForm()
        
        context = {
            "form": form,
        }
    
    return render(request, 'blog/add_post', context)


@login_required()
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



