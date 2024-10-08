from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_shop = models.BooleanField(default=False, verbose_name="Is Shop")
    is_user = models.BooleanField(default=False, verbose_name="Is User")
    name = models.CharField(max_length=100,null=True, blank=True)
    mobile = models.CharField(max_length=15,null=True, blank=True)
    address = models.CharField(max_length=200,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    GST = models.CharField(max_length=100,null=True, blank=True)
    photo = models.ImageField(upload_to='profile/')

    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return  url


class Worker(models.Model):
    shop = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shop', verbose_name="shop")
    name = models.CharField(max_length=100, verbose_name="worker Name",null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    mobile = models.CharField(max_length=15,null=True, blank=True)
    place = models.CharField(max_length=200,null=True, blank=True)
    images = models.ImageField(upload_to='worker_images/', null=True, blank=True, verbose_name="Product Images")
   
    @property
    def imageURL_1(self):
        try:
            url = self.images.url
        except:
            url = ''
        return  url
    

    def __str__(self):
        return self.name
    
    
class Package(models.Model):
    shop_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shop_1', verbose_name="shop_1")
    name = models.CharField(max_length=100, verbose_name="Package Name",null=True, blank=True)
    rate = models.IntegerField(null=True, blank=True)
    Warranty = models.CharField(max_length=100,null=True, blank=True)
    description = models.CharField(max_length=100, verbose_name="Description",null=True, blank=True)
   
    def __str__(self):
        return self.name

class Book(models.Model):
    shop_id = models.IntegerField(null=True, blank=True)
    shop_name = models.CharField(max_length=100, verbose_name="Shop Name",null=True, blank=True)
    shop_address = models.CharField(max_length=100, verbose_name="Shop address",null=True, blank=True)
    shop_phone = models.IntegerField(verbose_name="Shop phone",null=True, blank=True)
    packg_id = models.IntegerField(null=True, blank=True)
    packg_name = models.CharField(max_length=100,null=True, blank=True)
    warranty = models.IntegerField(null=True, blank=True)
    rate = models.IntegerField(null=True, blank=True)
    cust_id = models.IntegerField(null=True, blank=True)
    cust_name = models.CharField(max_length=100, verbose_name="Customer Name",null=True, blank=True)
    cust_address = models.CharField(max_length=100, verbose_name="Customer address",null=True, blank=True)
    cust_phone = models.IntegerField(verbose_name="Customer phone",null=True, blank=True)
    status = models.BooleanField(default=False)


    
class Message(models.Model):
    client_id = models.IntegerField(null=True, blank=True)
    site = models.CharField(max_length=100, verbose_name="Site Name",null=True, blank=True)
    worker = models.IntegerField(null=True, blank=True)
    date= models.DateField(null=True, blank=True)
    start = models.TimeField(null=True, blank=True)
    end = models.TimeField(verbose_name="end time",null=True, blank=True)
    images = models.ImageField(upload_to='Site images/', null=True, blank=True, verbose_name="Site Images")
   
class Bill(models.Model):
    shop_id = models.IntegerField(null=True, blank=True)
    client_id = models.IntegerField(null=True, blank=True)
    bill_no = models.IntegerField(null=True, blank=True)
    package_name = models.CharField(max_length=100, verbose_name="Package Name",null=True, blank=True)
    package_price = models.IntegerField(null=True, blank=True)
    shop_name= models.CharField(max_length=100, verbose_name="Shop Name",null=True, blank=True)
    shop_phone = models.IntegerField(null=True, blank=True)
    client_name = models.CharField(max_length=100, verbose_name="Client Name",null=True, blank=True)
    client_address = models.CharField(max_length=100, verbose_name="Client Address",null=True, blank=True)
    square_feet = models.CharField(max_length=100, verbose_name="Square Feet",null=True, blank=True)
    square_feet_rate =  models.IntegerField(null=True, blank=True)
    product_name = models.CharField(max_length=100, verbose_name="Site Name",null=True, blank=True)
    total_price=  models.IntegerField(null=True, blank=True)
   



    
    
