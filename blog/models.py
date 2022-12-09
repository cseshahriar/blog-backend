from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from .utils import BaseAttribute
from .utils import generate_unique_slug


class Category(BaseAttribute):
    parent = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True,
        related_name='children'
    )
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(self.title) != self.slug:
                self.slug = generate_unique_slug(Category, self.title)
        else:  # create
            self.slug = generate_unique_slug(Category, self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(BaseAttribute):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(self.title) != self.slug:
                self.slug = generate_unique_slug(Tag, self.title)
        else:  # create
            self.slug = generate_unique_slug(Tag, self.title)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


def article_upload_path(instance, filename):
    """Returns formatted upload to path"""
    return f'article/{instance.id}/{filename}'


class Article(BaseAttribute):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='articles'
    )
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to=article_upload_path)
    meta_keywords = models.TextField(blank=False)
    published_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft'
    )

    class Meta:
        ordering = ['-published_at']

    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(self.title) != self.slug:
                self.slug = generate_unique_slug(Article, self.title)
        else:  # create
            self.slug = generate_unique_slug(Article, self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(BaseAttribute):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments'
    )
    content = models.TextField(blank=False)

    def __str__(self):
        return str(self.article.title)
