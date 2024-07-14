from django.db import models
from django.contrib.auth.models import User





class Stocks(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, default='default')
    price = models.FloatField(default=0)
    number = models.IntegerField(default=0)
    
    def __str__(self): 
        return self.name
    
    

    

    
