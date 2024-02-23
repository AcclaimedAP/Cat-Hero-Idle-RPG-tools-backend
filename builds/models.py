from django.db import models
from django.utils import timezone
import datetime
import string
import random


def generate_random_id():
    return ''.join(random.choices(string.ascii_uppercase, k=6))


class BuildModel(models.Model):
    id = models.CharField(max_length=6, primary_key=True,
                          default=generate_random_id, editable=False)
    build_string = models.CharField(max_length=9000)
    created = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.build_string

    @property
    def unused(self):
        return self.last_accessed <= timezone.now() - datetime.timedelta(days=30)
