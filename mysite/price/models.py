from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.utils import timezone


class  Item(models.Model):
    name = models.CharField('Name', max_length=200)
    price = models.IntegerField('Price')
    quantity = models.IntegerField('Quantity', default=0)
    sold_quantity = models.IntegerField('Sold Quantity', default=0)
    pub_date = models.DateTimeField('date added', default=timezone.now())

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
