from django.db import models  # noqa
from .utils import BaseAttribute


class Article(BaseAttribute):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
