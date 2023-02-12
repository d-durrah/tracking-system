from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "categories"