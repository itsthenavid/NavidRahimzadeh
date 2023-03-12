from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ClustersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clusters'

    # Translation and names
    verbose_name = _("Clusters")
