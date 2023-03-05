from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

# You can create Forms or ModelForms here.


class CustomUserCreationForm(UserCreationForm):
    """
    This form determines how to create a user.
    It can include registration.
    """

    class Meta:
        model = CustomUser
        fields = (
            "avatar",
            "first_name",
            "last_name",
            "username",
            "email",
            "bio",
        )


class CustomUserChangeForm(UserChangeForm):
    """
    This form is based on the Customuser model for changing user information. 
    It can also be used for profiles.
    """

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
