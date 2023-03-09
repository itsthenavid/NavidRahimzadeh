from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.utils.html import format_html

from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

from extensions.utils import get_jalali_datetime

# Create your models here.


class Category(models.Model):
    """
    This model is written to categorize different posts that will be stored 
    in the Post model.

    Please note that this model is different from Tag models.
    """

    # Database fields
    name = models.CharField(
        _("Category Name"),
        max_length=225,
        help_text=_(
        "You can choose a name for this category. "
        "This name is displayed when a post is read."
        )
    )
    content = models.TextField(
        _("Category Content"),
        blank=True,
        help_text=_(
        "The description of this category can have a "
        "great impact on the process of editing, "
        "deleting, adding and naming it."
        )
    )
    is_active = models.BooleanField(
        _("Active"),
        default=True,
        help_text=_(
        "The \"Active\" option can stop posts from "
        "being shown to the public."
        )
    )

    # Class Meta Classes

    class Meta:
        """
        This class contains settings related to the Category Model.

        Settings such as translations, arrangement, etc. are designed in this
        Class.
        """

        # Translation and names
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    # Class Magic Methods

    def __str__(self) -> str:
        return str(f"{self.name}")
    
    def __repr__(self) -> str:
        return str(f"{self.name}")
    
    def __unicode__(self) -> str:
        return str(f"{self.name}")
