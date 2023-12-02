from django.db import models
from django.utils import timezone

# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length = 30)
    date = models.DateTimeField(auto_now_add = True, blank = True)
    embed_code = models.CharField(max_length = 40)