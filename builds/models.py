from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class BuildString(models.Model):

    build_string = models.CharField(max_length=9000)
    created = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.build_string
    
    def unused(self):
        return self.last_accessed <= timezone.now() - datetime.timedelta(days=30)


