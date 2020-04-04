from __future__ import absolute_import
import random

from celery import Celery
from newsdph import DEFAULT_APP_NAME
from newsdph.settings import CeleryConfig


proj = Celery(DEFAULT_APP_NAME)
proj.config_from_object(CeleryConfig)
