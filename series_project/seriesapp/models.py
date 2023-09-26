from django.db import models

# Create your models here.
class tvseries(models.Model):
    name=models.CharField(max_length=250)
    year=models.IntegerField()
    desc=models.TextField()
    img=models.ImageField(upload_to='picture')

    def __str__(self):
        return self.name