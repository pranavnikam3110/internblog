from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads',blank=True)
    content = HTMLField()


    def __str__(self):
        return self.title


