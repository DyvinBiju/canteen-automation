from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class FoodItems(models.Model):
    food_items = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    s_id = models.ForeignKey(User,on_delete=models.CASCADE)
    

    