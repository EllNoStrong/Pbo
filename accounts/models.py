from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    ('customer', 'Customer'),
    ('driver', 'Driver'),
    ('restaurant', 'Restaurant'),
    ('admin', 'Admin'),
)


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrator'),
        ('restaurant', 'Restaurant'),
        ('driver', 'Driver'),
        ('customer', 'Customer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    # Untuk restoran/driver perlu disetujui dulu oleh admin
    is_approved = models.BooleanField(default=False)

    def is_admin(self):
        return self.is_superuser or self.role == 'admin'

# Profil opsional untuk data tambahan
class RestaurantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='restaurant_profile')
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    # status buka/tutup bisa di model ini
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class DriverProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver_profile')
    phone = models.CharField(max_length=50, blank=True, null=True)
    vehicle_info = models.CharField(max_length=255, blank=True, null=True)
    # contoh field skors / punishment counter
    suspended_until = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Driver {self.user.username}"

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    phone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Customer {self.user.username}"

# Create your models here.
