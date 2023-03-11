# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect

from .models import Post, Comment
from .forms import CommentForm

# Create your views here.


class PostListView(ListView):
    """
    Send a list of active posts to blog/post_list.html and prepare to 
    appear in the URL
    """
    model = Post
    queryset = Post.actives.all()
    template_name = "blog/post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    """
    Send one of the active posts to blog/post_detail and display user 
    comments, receive user comments
    """
    model = Post
    queryset = Post.actives
    template_name = "blog/post_detail.html"
    slug_field = "slug"

    # Class Methods

    def get_context_data(self, *args, **kwargs):
        # Get old method information
        data = super().get_context_data(*args, **kwargs)
        # Get comments of the post
        connected_comments = Comment.objects.filter(post=self.get_object())
        # Counting comments
        number_of_comments = connected_comments.count()
        # Send the received information to contexts
        data['comments'] = connected_comments
        data['number_of_comments'] = number_of_comments
        data['comment_form'] = CommentForm()
        return data

    def post(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            # Creating a new form and checking the validity of the form
            comment_form = CommentForm(self.request.POST)
            if comment_form.is_valid():
                comment = comment_form.cleaned_data['comment']
                # Check if the reply is sent or not
                try:
                    parent = comment_form.cleaned_data['parent']
                except:
                    parent = None

            
            # Creating a new comment based on the submission data 
            # received from POST
            new_comment = Comment(
                comment=comment, commenter=self.request.user, post=self.get_object(), 
                parent=parent
            )
            new_comment.save()
            # Return the user to the page
            return HttpResponseRedirect(self.request.path_info)
