from django.db import models
from django.utils.translation import gettext_lazy as _

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
        max_length=225
    )
    content = models.TextField(
        _("Category Content"),
        blank=True
    )
    is_active = models.BooleanField(
        _("Active"),
        default=True
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
