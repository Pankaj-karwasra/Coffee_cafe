from django.db import models

# Create your models here.
class OurStory(models.Model):
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title