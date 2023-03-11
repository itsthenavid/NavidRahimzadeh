from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

from extensions.utils import get_jalali_datetime, get_jalali_date
from .managers import ActivePostManager

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
    

class Post(models.Model):
    """
    This class is one of the most important classes of the project. 
    In fact, this class includes the site posts that are displayed. 
    This class should be developed in an extremely specialized and 
    sensitive manner.

    This class contains many fields, some of which are up to SRS and the 
    rest based on the developer's choices along the way.
    """

    # Database constants
    _STATUS_CHOICES = (
        (str(0), _("Draft"), ), 
        (str(1), _("Published"), ), 
    )

    # Database fields
    banner = models.ImageField(
        _("Post Banner"),
        default="defaults/post_banner.webp",
        upload_to="blog/posts/",
        help_text=_(
        "The post banner is a field that is shown to "
        "the user next to the post title in any case "
        "and is completely different from other "
        "photos of the post content."
        )
    )
    title = models.CharField(
        _("Title"),
        max_length=225,
        unique=True,
        help_text=_(
        "The title of the post does not need "
        "additional explanation, just remind me "
        "that it should be short and concise."
        ),
    )
    description = models.CharField(
        _("Post Description"),
        max_length=885,
        blank=True,
        unique=True,
        help_text=_(
        "The description of this post is shown "
        "for SEO and as a summary of this post "
        "and its content in the list of posts. "
        "The quality of literature and writing "
        "in this field is very important."
        ),
    )
    slug = models.SlugField(
        _("Slug"),
        max_length=225,
        allow_unicode=True,
        unique=True,
        help_text=_(
        "Slugs are fields for addressing and are "
        "very important in SEO as well as site "
        "performance. Preferably, Slug should be "
        "English and meaningful."
        ),
    )
    category = models.ForeignKey(
        verbose_name=_("Post Category"),
        to=Category,
        on_delete=models.SET_NULL,
        null=True,
        help_text=_(
        "Choose a category related to the content "
        "of the post for the post."
        )
    )
    datetime_created = models.DateTimeField(
        _("Datetime Created"),
        auto_now_add=True,
        auto_now=False
    )
    datetime_modified = models.DateTimeField(
        _("Datetime Modified"),
        auto_now_add=False,
        auto_now=True
    )
    author = models.ForeignKey(
        verbose_name=_("Author"),
        to=get_user_model(),
        on_delete=models.SET_NULL,
        null=True
    )
    content = RichTextUploadingField(
        _("Post Content"),
        blank=True,
        help_text=_(
        "This part of the post is the body and full "
        "content of the post. Here you are not limited "
        "by any special rules and you can type as much "
        "as you want. Remember, your only limitation is "
        "offensive words. It is not acceptable to post "
        "offensive words on the site. Apart from this, "
        "in addition to the text, you can upload any "
        "file you want."
        )
    )
    pub_datetime = models.DateTimeField(
        _("Publish Datetime"),
        default=now,
        blank=True,
        null=True,
    )
    tags = TaggableManager(
        _("Tags"),
        blank=True
    )
    status = models.CharField(
        _("Status"),
        max_length=1,
        choices=_STATUS_CHOICES,
        default=_STATUS_CHOICES[0][0],
    )
    is_active = models.BooleanField(
        _("Active"),
        default=True,
        help_text=_(
        "The \"Active\" option can stop posts from "
        "being shown to the public."
        )
    )
    # Managers
    objects = models.Manager()
    actives = ActivePostManager()

    # Class Subclasses

    class Meta:
        """
        This class is designed to change the default settings of this model.
        """

        # Translation and names
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    # Class Methods

    def get_post_banner_thumbnail(self):
        """
        Returning a thumbnail to show on admin panel and more.
        """
        return format_html(
            """
            <img src="{}" style="height: 100px; width: 150px;" />
            """.format(self.banner.url)
        )
    get_post_banner_thumbnail.short_description = _("Post Banner")

    def get_jalali_pub_datetime(self):
        return get_jalali_datetime(self.pub_datetime)
    get_jalali_pub_datetime.short_description = _("Publish Datetime")

    def get_jalali_pub_date(self):
        return get_jalali_date(self.pub_datetime)
    get_jalali_pub_date.short_description = _("Publish Date")

    def get_absolute_url(self):
        """
        Main address of Model.

        Using for SEO, URL management and more.
        """
        return reverse("blog:post_detail", kwargs={"slug": self.slug})
    
    # Class Magic Methods

    def __str__(self) -> str:
        return str(f"{self.title}")
    
    def __repr__(self) -> str:
        return str(f"{self.title}")
    
    def __unicode__(self) -> str:
        return str(f"{self.title}")
    

class Comment(models.Model):
    """
    This model is part of the sub-models of the project, but it is very 
    efficient. Comments are displayed in a branched thread. Each comment  
    is related to one post and one author, so that no author other than  
    the original author of the comment has the right to edit and  
    manipulate the comment. In the first phase of the project, this part  
    will definitely not be that advanced, but remember this model.

    This model should be designed very simply and at the same time 
    efficiently. In addition, it should include the Reply feature 
    in a branch form.
    """

    # Database fields
    post = models.ForeignKey(
        verbose_name=_("Post"),
        to=Post,
        on_delete=models.CASCADE,
        related_name="post_comments"
    )
    datetime_created = models.DateTimeField(
        _("Datetime Created"),
        auto_now_add=True,
        auto_now=False
    )
    datetime_modified = models.DateTimeField(
        _("Datetime Modified"),
        auto_now_add=False,
        auto_now=True
    )
    commenter = models.ForeignKey(
        verbose_name=_("Commenter"),
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name="user_comments",
    )
    comment = models.TextField(
        _("Comment"),
    )
    parent = models.ForeignKey(
        verbose_name=_("Reply"),
        to='self',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="replies"
    )
    is_active = models.BooleanField(
        _("Active"),
        default=True
    )

    # Class Subclasses

    class Meta:
        """
        This class is initialized to customize the settings of the Comment 
        model.
        """
        # Ordering system
        ordering = ("-datetime_modified", "-datetime_created", )

        # Translation and names
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    # Class Methods

    @property
    def children(self):
        """
        Returning replay comments‍
        """
        return Comment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
    
    def get_jalali_datetime_created(self):
        return get_jalali_datetime(self.datetime_created)
    get_jalali_datetime_created.short_description = _("Datetime Created")

    # Class Magic Methods

    def __str__(self) -> str:
        return str(f"{self.commenter}")
    
    def __repr__(self) -> str:
        return str(f"{self.commenter}")
    
    def __unicode__(self) -> str:
        return str(f"{self.commenter}")
