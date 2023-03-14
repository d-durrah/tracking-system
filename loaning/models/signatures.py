from django.db import models
from loaning.models import Log

class Signature(models.Model):
    signature = models.FileField(upload_to ='uploads/signature_archive')
    log_id = models.ForeignKey(Log,on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.id)