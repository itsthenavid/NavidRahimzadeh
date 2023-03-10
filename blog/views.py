from django.shortcuts import render

from .models import Post

# Create your views here.


def post_list_view(request):
    post_list = Post.actives.all()

    context = {
        "posts": post_list,
    }
    return render(request, "blog/post_list.html", context)


def post_detail_view(request, slug):
    post = Post.actives.get(slug=slug)

    context = {
        "post": post,
    }
    return render(request, "blog/post_detail.html", context)
