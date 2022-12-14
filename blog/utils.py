from django.db import models
from users.models import User
from django.utils.text import slugify


def generate_unique_slug(klass, field, instance=None):
    """
    return unique slug if origin slug is exist.
    eg: `foo-bar` => `foo-bar-1`
    :param `klass` is Class model.
    :param `field` is specific field for title.
    :param `instance` is instance object for excluding specific object.
    """
    origin_slug = slugify(field)
    unique_slug = origin_slug
    numb = 1
    if instance is not None:
        while klass.objects.filter(slug=unique_slug).exclude(id=instance.id).exists():  # noqa
            unique_slug = '%s-%d' % (origin_slug, numb)
            numb += 1
    else:
        while klass.objects.filter(slug=unique_slug).exists():
            unique_slug = '%s-%d' % (origin_slug, numb)
            numb += 1
    return unique_slug


class BaseAttribute(models.Model):
    """ base date fields"""
    created_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="%(app_label)s_%(class)s_created_user"
    )
    updated_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="%(app_label)s_%(class)s_updated_by"
    )
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
