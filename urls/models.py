from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class URL(models.Model):
    long_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=100, unique=True)
    visit_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.short_url} - > {self.long_url}'