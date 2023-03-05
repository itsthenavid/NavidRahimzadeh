from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

from random import choice

from extensions.utils import get_jalali_datetime

# Create your models here.


def _set_user_default_avatar():
    """
    This method selects and returns a avatar from the 10 different avatars.
    """
    
    avatars = (
        "user_avatar_1.webp",
        "user_avatar_2.webp",
        "user_avatar_3.webp",
        "user_avatar_4.webp",
        "user_avatar_5.webp",
        "user_avatar_6.webp",
        "user_avatar_7.webp",
        "user_avatar_8.webp",
        "user_avatar_9.webp",
        "user_avatar_10.webp",
        "user_avatar_11.webp",
        "user_avatar_12.webp",
        "user_avatar_13.webp",
        "user_avatar_14.webp",
        "user_avatar_15.webp",
        "user_avatar_16.webp",
        "user_avatar_17.webp",
        "user_avatar_18.webp",
        "user_avatar_19.webp",
    )

    return choice(avatars)


class CustomUser(AbstractUser):
    """
    This class is built to manage user accounts with a different model than 
    the default Django model.

    This model manages tasks like login, signup and the like.
    """

    # Database fields
    avatar = models.ImageField(
        _("Avatar"),
        default=f"defaults/{_set_user_default_avatar()}",
        upload_to="accounts/avatars/"
    )
    nickname = models.CharField(
        _("Nickname"),
        max_length=55,
        blank=True
    )
    bio = models.TextField(
        _("Biography"),
        blank=True
    )
    is_premium = models.BooleanField(
        _("Premium"),
        default=False
    )

    # Class methods

    def get_user_display_name(self) -> str:
        """
        You may have specified the surname, name, nickname, username, email or 
        all of them. 
        
        This method determines what the first is to be shown.
        """

        if self.nickname:
            return str(f"{self.nickname}")
        elif self.first_name and self.last_name:
            return str(f"{self.first_name} {self.last_name}")
        elif self.first_name:
            return str(f"{self.first_name}")
        elif self.last_name:
            return str(f"{self.last_name}")
        elif self.username:
            return str(f"{self.username}")
        else:
            return str(f"{self.email}")
    get_user_display_name.short_description = _("The Display Name")
        
    def get_user_avatar_thumbnail(self):
        """
        This avatar method creates a small thumb for each user.

        This method can be displayed as an element in `list_display` in the 
        admin panel.
        """

        avatar_thumbnail = format_html(
            """
            <img src="{}" style="height: 65px; width: 65px; border-radius: 50%;" />
            """.format(self.avatar.url)
        )

        return avatar_thumbnail
    get_user_avatar_thumbnail.short_description = _("Avatar")

    def get_user_jalali_date_joined(self):
        return get_jalali_datetime(self.date_joined)
    get_user_jalali_date_joined.short_description = _("Date Joined")
    
    # Class Magic Methods

    def __str__(self) -> str:
        return str(f"{self.get_user_display_name()}")
    
    def __repr__(self) -> str:
        return str(f"{self.get_user_display_name()}")
    
    def __unicode__(self) -> str:
        return str(f"{self.get_user_display_name()}")
