from django.db import models

# Create your models here.
class FileUpload(models.Model):
    name=models.CharField(max_length=255)
    create = models.ImageField(upload_to='imag/')