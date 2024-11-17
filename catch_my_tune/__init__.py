from __future__ import absolute_import, unicode_literals

# Celery uygulamasını projeyle entegre ediyoruz
from .celery_app import app as celery_app

__all__ = ('celery_app',)
