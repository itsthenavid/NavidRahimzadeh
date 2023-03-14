from django.db.models import Manager
from django.utils.timezone import now

# Create Model Managers here.


class ActivePostManager(Manager):
    """
    This class is a Manager designed for the Post model. In fact, this 
    class helps to display only the posts with display conditions in the 
    post list.
    """

    def get_queryset(self):
        return super(ActivePostManager, self).get_queryset()\
        .exclude(is_active=False).filter(pub_datetime__lte=now())\
            .exclude(status=str(0)).filter(category__is_active=True)
