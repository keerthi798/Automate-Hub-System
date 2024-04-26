from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from datetime import datetime


from django.db import models

class CustomUser(AbstractUser):
     # Add any additional fields you need
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True) 
    role = models.CharField(max_length=100,default="")
    def change_password(self, new_password):
        self.set_password(new_password)
        self.save()

    def _str_(self):
        return self.username


class ServiceBooking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    driver_number = models.CharField(max_length=15)
    vehicle_number = models.CharField(max_length=15)
    service_branch = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=50)
    service_type = models.CharField(max_length=10)
    service_date = models.DateField()
    email = models.EmailField(default='')
    file_upload = models.FileField(upload_to='uploads/', null=True, blank=True)
    time_slot = models.DateTimeField(default="", null=True)

    def __str__(self):
        return f"Service Booking for {self.user.email if self.user else 'No User'}"
    
class InsuranceRenewal(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    register_number = models.CharField(max_length=20)
    insurance_number = models.CharField(max_length=20)
    insurance_expire_date = models.DateField()
    state = models.CharField(max_length=50)
    service_branch = models.CharField(max_length=50)
    id_proof = models.FileField(upload_to='id_proofs/', blank=True, null=True)


class InsuranceNew(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    register_number = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    id_proof = models.FileField(upload_to='id_proofs/', blank=True, null=True)

class Parts(models.Model):
    partsname = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    parts_image = models.ImageField(upload_to='part_images/')
    quantity = models.PositiveIntegerField(default=0)
    categories = models.CharField(max_length=100, null=True, blank=True, default='Uncategorized')
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    additional_details = models.TextField(blank=True, null=True)
    
    
    def __str__(self):
        return self.partsname
    
class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Parts, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    
    def str(self):
         return self.username   


class CartItem1(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('Parts', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
    

class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Parts, through='CartItem1')

    def __str__(self):
        return f"Cart for {self.user.username}"   
class Order(models.Model):
    DELIVERY_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('OUT_FOR_DELIVERY', 'Out for Delivery'),
        ('DELIVERED', 'Delivered'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Parts, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    payment_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_status = models.CharField(max_length=20, choices=DELIVERY_STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Parts, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"
    
#vehicle_add
    
# partsapp/models.py



class Vehicle(models.Model):
    VEHICLE_MODELS = [
        ('lightvehicle', 'Light Vehicle'),
        ('trucks', 'Trucks'),
        ('buses', 'Buses'),
    ]

    VEHICLE_USAGES = [
        ('goodscarriers', 'Goods Carriers'),
        ('passenger', 'Passenger'),
    ]

    VEHICLE_APPLICATIONS = [
        ('beverage', 'Beverage'),
        ('buildingmaterial', 'Building Material'),
        ('constructionhardware', 'Construction and Hardware'),
        ('fishery', 'Fishery'),
        ('fruits_vegetables', 'Fruits and Vegetables'),
        ('industrial_goods', 'Industrial Goods'),
        ('lpg_distribution', 'LPG Distribution'),
        ('school_transport', 'School Transport'),
        ('tours_travels', 'Tours and Travels'),
    ]

    FUEL_TYPES = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('cng', 'CNG'),
        ('electric', 'Electric'),
    ]

    TRANSMISSION_TYPES = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
        ('semiautomatic', 'Semi-Automatic'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    vehicle_model = models.CharField(max_length=20, choices=VEHICLE_MODELS)
    vehicle_usage = models.CharField(max_length=20, choices=VEHICLE_USAGES)
    vehicle_application = models.CharField(max_length=20, choices=VEHICLE_APPLICATIONS)
    fuel_type = models.CharField(max_length=10, choices=FUEL_TYPES)
    transmission_type = models.CharField(max_length=15, choices=TRANSMISSION_TYPES)
    engine_size = models.IntegerField(blank=True, null=True)
    mileage = models.FloatField(blank=True, null=True)
    warranty = models.CharField(max_length=100, blank=True, null=True)
    seating_capacity = models.IntegerField(blank=True, null=True)
    fuel_tank_capacity = models.FloatField(blank=True, null=True)
    vehicle_colors = models.JSONField(default=list, blank=True, null=True)
    stock = models.IntegerField(default=0)
    brochure = models.FileField(upload_to='vehicle_brochures/', blank=True, null=True)
    booking_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name
class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='vehicle_images/', blank=True, null=True)


class Booking(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    booking_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    booking_time = models.DateTimeField(default=datetime.now, blank=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Delivered', 'Delivered')], default='Pending')
    
#insurance
class Insurance(models.Model):
    vehicle_model = models.CharField(max_length=20)
    vehicle_usage = models.CharField(max_length=20)
    fuel_type = models.CharField(max_length=20)
    transmission_type = models.CharField(max_length=20)
    insurance_type = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    renew_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.vehicle_model} - {self.vehicle_usage} - {self.insurance_type}"

#deleted data store table
    
class DeletedInsurance(models.Model):
    vehicle_model = models.CharField(max_length=20)
    vehicle_usage = models.CharField(max_length=20)
    fuel_type = models.CharField(max_length=20)
    transmission_type = models.CharField(max_length=20)
    insurance_type = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    renew_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.vehicle_model} - {self.vehicle_usage} - {self.insurance_type}"
    
class PreviousInsurance(models.Model):
    original_insurance = models.ForeignKey('Insurance', on_delete=models.CASCADE)
    vehicle_model = models.CharField(max_length=20)
    vehicle_usage = models.CharField(max_length=20)
    fuel_type = models.CharField(max_length=20)
    transmission_type = models.CharField(max_length=20)
    insurance_type = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    renew_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Previous data for {self.vehicle_model} - {self.vehicle_usage} - {self.insurance_type}"
from django.utils.translation import gettext_lazy as _
    
class WishlistItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'vehicle')


class ConfirmedVehicle(models.Model):
    
    vehicle_name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    booking_amount = models.DecimalField(max_digits=10, decimal_places=2)
    booking_time = models.DateTimeField()
    registration = models.ForeignKey('VehicleRegistration', on_delete=models.SET_NULL, null=True, blank=True)

class VehicleRegistration(models.Model):
    registration_number = models.CharField(max_length=20)
    

    def __str__(self):
        return self.registration_number
from django.utils import timezone 
from django.db import models

class PaymentRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    insurancenew = models.ForeignKey(InsuranceNew, on_delete=models.CASCADE, null=True)
    payment_datetime = models.DateTimeField(default=timezone.now)
    confirmed = models.BooleanField(default=False)
    
class Policy(models.Model):
    number = models.CharField(max_length=20, unique=True)
    issued_date = models.DateField()
    expiry_date = models.DateField()
    

    def __str__(self):
        return self.number

from django.db import models
from django.contrib.auth.models import User

class ConfirmedInsurance(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    register_number = models.CharField(max_length=20)
    policy_number = models.CharField(max_length=20)
    start_date = models.DateField()
    expire_date = models.DateField()

    def __str__(self):
        return f"{self.user.username}'s Confirmed Insurance"


