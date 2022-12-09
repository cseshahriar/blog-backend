# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Category, Tag, Article, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_user',
        'updated_user',
        'is_active',
        'created_at',
        'updated_at',
        'parent',
        'title',
        'slug',
        'description',
    )
    list_filter = (
        'created_user',
        'updated_user',
        'is_active',
        'created_at',
        'updated_at',
        'parent',
    )
    search_fields = ('slug',)
    date_hierarchy = 'created_at'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_user',
        'updated_user',
        'is_active',
        'created_at',
        'updated_at',
        'title',
        'slug',
        'description',
    )
    list_filter = (
        'created_user',
        'updated_user',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = ('slug',)
    date_hierarchy = 'created_at'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_user',
        'updated_user',
        'is_active',
        'created_at',
        'updated_at',
        'category',
        'title',
        'slug',
        'description',
        'thumbnail',
        'meta_keywords',
        'published_at',
        'status',
    )
    list_filter = (
        'created_user',
        'updated_user',
        'is_active',
        'created_at',
        'updated_at',
        'category',
        'published_at',
    )
    raw_id_fields = ('tags',)
    search_fields = ('slug',)
    date_hierarchy = 'created_at'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_user',
        'updated_user',
        'is_active',
        'created_at',
        'updated_at',
        'article',
        'content',
    )
    list_filter = (
        'created_user',
        'updated_user',
        'is_active',
        'created_at',
        'updated_at',
        'article',
    )
    date_hierarchy = 'created_at'
