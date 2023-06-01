# Configuration settings for apps included in this Django implementation

from django.apps import AppConfig


class PlaygroundConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'playground'
