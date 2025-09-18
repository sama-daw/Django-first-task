from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    article = models.TextField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title