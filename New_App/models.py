from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Size(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    size = models.CharField(max_length=50, choices=(
                                                    ('S', 'S'),
                                                    ('M', 'M'),
                                                    ('L', 'L'),
                                                    ('XL', 'XL'),
                                                    ('XXL', 'XXL')))
    
    
    def __str__(self):
        return self.size
    
    