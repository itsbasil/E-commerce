from django.db import models

# Create your models here.

# Model for Product
class Product(models.Model):
    title=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='/media')
    priority=models.IntegerField(default=0)