from django.db import models
from accounts.models import User
# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE)
    driver = models.ForeignKey('drivers.Driver', null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
