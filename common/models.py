import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='ID')

    class Meta:
        abstract = True


class TimedModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Создано в'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Обновлено в'))

    class Meta:
        abstract = True


class TimedModel(BaseModel, TimedModelMixin):
    class Meta:
        abstract = True
