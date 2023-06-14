from django.db import models

# Create your models here.
class gaurd(models.Model):
    gname = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gpass = models.CharField(max_length=100)
    
    def __str__(self):
        return self.fname
 
class guest_detail(models.Model):
    intime = models.CharField(max_length=100)
    extime = models.CharField(max_length=100)
    guest = models.CharField(max_length=100)
    pur = models.CharField(max_length=100)
    camefrom = models.CharField(max_length=100)
    
    def __str__(self):
        return self.guest
