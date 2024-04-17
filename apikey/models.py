from django.db import models
import uuid


class ApiKey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.CharField(max_length=100)
    usage_count = models.IntegerField(default=0)
    usable = models.BooleanField()

    def __str__(self):
        return f"{self.user} - {self.id}"
