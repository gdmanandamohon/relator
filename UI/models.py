from django.db import models
from datetime import datetime
from Realtor.models import Realtor

# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=250)
    zipcode = models.CharField(max_length=6)
    description = models.TextField(max_length=5000)
    price = models.FloatField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    bedrooms = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    is_published = models.BooleanField(default=False)
    updated_time = models.DateField(default=datetime.now)
    
    def __init__(self):
        return self.title

