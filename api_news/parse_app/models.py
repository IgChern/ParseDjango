from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    created = models.DateTimeField()
    created_in_db = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
