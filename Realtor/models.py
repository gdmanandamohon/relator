from django.db import models
from django.db.models.expressions import OrderBy
from django.db.models.query_utils import PathInfo
from datetime import date, datetime

# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=250)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    email = models.EmailField(blank= False)
    phone = models.CharField(max_length= 11)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateField(default=datetime.now)

    def __init__(self):
        return self.name
