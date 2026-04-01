import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    """
    Modelo base para entidades do sistema.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid7, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT, 
        related_name='owned_%(class)s'
    )

    @property
    def is_deleted(self):
        return self.deleted_at is not None

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True
