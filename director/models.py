from django.db import models

# Create your models here.

class database(models.Model):
     
    dname = models.CharField(max_length=100)
    dpass = models.CharField(max_length=50)
    
    def __str__(self):
        return self.dname
        
    



