from django.forms import ModelForm

from .models import Comment

# Create custom Forms or ModelForms here.


class CommentForm(ModelForm):
    """
    """

    # Class Subclasses

    class Meta:
        """
        """
        model = Comment
        fields = (
            "comment",
            "parent",
        )
