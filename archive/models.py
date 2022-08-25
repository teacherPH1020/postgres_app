from django.db import models

# Create your models here.
class Storage(models.Model):
    cell = models.TextField()
    file = models.FileField()
    access_date = models.DateTimeField()

class Metadata(models.Model):
    cell_pk = models.ForeignKey(Storage, on_delete=models.CASCADE)
    info = models.CharField(max_length=256)
    date = models.DateField()