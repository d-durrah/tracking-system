from django.db import models
from management.models.add_device import Device
from django.db.models.base import Model

# Create your models here.

class Resource_Sign_Out(models.Model):
    resource_asset_number = models.ForeignKey(Device, on_delete=models.CASCADE,default=1)
    item_description = models.TextField(max_length=900, blank=False)
    purpose = models.TextField(max_length=900, blank=False)
    ID_number = models.IntegerField()

    def __int__(self):
        return self.resource_asset_number

# Creating a form to change an existing article.
article = Article.objects.get(pk=1)
form = ArticleForm(instance=article)