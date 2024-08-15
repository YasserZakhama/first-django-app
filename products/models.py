from django.db import models
from datetime import datetime
# Create your models here.

class Product(models.Model):
    x=[
        ('Ma3dani','Ma3dani'),
        ('Soda','Soda'),
        ('Chrab','Chrab'),
    ]

    name=models.CharField(max_length=50,default='Lesm')
    content=models.TextField(null=True,blank=True,default='Ousef mantoujek')
    price=models.DecimalField(max_digits=5, decimal_places=2,default=0.00)
    image=models.ImageField(upload_to='photo/%y/%m/%d')
    ca=models.CharField(max_length=50,verbose_name='Category',null=True,blank=True, choices=x)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Hajat tetchrab'
        #ordering = ['-price']

class Time(models.Model):
    now=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return "NOW"