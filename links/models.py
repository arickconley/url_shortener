from django.contrib.auth.models import User
from django.db import models

from .utils import dehydrate


# Create your models here.
class Link(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="links")
    title = models.CharField(max_length=240, null=True)
    description = models.TextField(null=True)
    url = models.URLField(max_length=250)
    views = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True)

    @property
    def guid(self):
        return f"{dehydrate(self.id)}"

    def add_view(self):
        self.views = self.views + 1
        self.save()

    def __str__(self) -> str:
        return f"{self.guid}"
