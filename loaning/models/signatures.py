from django.db import models

class Signature(models.Model):
    signature = models.FileField(upload_to ='uploads/signature_archive')

    def __str__(self):
        return str(self.id)