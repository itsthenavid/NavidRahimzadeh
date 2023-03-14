from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist

from .models import Post, Comment
from .forms import CommentForm

# Create your views here.


def post_list_view(request):
    """
    This function is used to display the list of posts in real time.

    Posts in this function are developed using actives (Manager) filter.

    Finally, the posts are shown in the templates after passing the 
    ActivesPostManager filters.
    """
    # Get posts that are eligible to be displayed.
    posts = Post.actives.all()

    # Compilation and rendering of data
    context = {
        "posts": posts,
    }
    return render(request, "blog/post_list.html", context)


def post_detail_view(request, slug):
    """
    This function is responsible for sending a post with details to the 
    template based on the slug requested by the user 
    (may be sent from a list).

    Notes about the function:
    1. This function should support 404 error.
    2. The post returned by this function must be one of the active posts.
    3. Send a comprehensive view of the post model and comments to the format.
    4. Can receive comments
    """
    try:
        # Attempt to find the requested post based on the slug given by 
        # the user
        post = Post.actives.get(slug=slug)
        # If successful, collecting comments and their number
        connected_comments = Comment.objects.filter(is_active=True)\
            .filter(post=post)
        number_of_comments = connected_comments.count()
    except ObjectDoesNotExist:
        # Raise 404 status code if the requested post does not exist
        raise Http404

    # Check the request type
    if request.method == "POST":
        # Creating a form based on the information sent (POST).
        form = CommentForm(request.POST)
        if form.is_valid():
            # If the quality of the security and information of the form is 
            # correct, start saving the data...
            # Some information must be filled in by the developer himself
            # So: "commit=False". Now we can save some data.
            comment = form.save(commit=False)
            try:
                # If the print field was sent from the template, we will fill it.
                comment.parent = form.cleaned_data["parent"]
            except:
                comment.parent = None
            # Next, the author of the comment and the post related to the comment 
            # will be added.
            comment.commenter = request.user
            comment.post = post
            comment.save()
            # After saving the comment, basically a refresh is done to the main 
            # page.
            return HttpResponseRedirect(request.path_info)
        else:
            # If the information is incorrect and their security accuracy is not 
            # confirmed, the return to the main page will begin.
            return HttpResponseRedirect(request.path_info)
    else:
        # If the request is GET, we dedicate an empty form.
        form = CommentForm()

    context = {
        "post": post,
        "comments": connected_comments,
        "number_of_comments": number_of_comments,
        "form": form
    }
    return render(request, "blog/post_detail.html", context)
