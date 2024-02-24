from django.db import models


class News(models.Model):
    TYPE_CHOICES = [
        ('website', 'Website News'),
        ('game', 'Game News'),
        ('discord', 'Discord News'),
        ('guides', 'Guides'),
        ('other', 'Other'),
    ]
    slug = models.SlugField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    author = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
