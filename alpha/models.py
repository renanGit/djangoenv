from django.db import models

# Create your models here.

class AlphaBoard(models.Model):
    title = models.CharField(max_length=50)
    alpha_text = models.CharField(max_length=2000)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

