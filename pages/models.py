from django.db import models
""" 
#OneToOne
class Female(models.Model):
    name_female=models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.name_female
class Male(models.Model):
    name_male=models.CharField(max_length=10,null=True)
    girls=models.OneToOneField(Female, on_delete=models.CASCADE)
    def __str__(self):
        return self.name_male
""" 
"""    
#OneToMany
class Phone(models.Model):
    name=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name
class User(models.Model):
    name=models.CharField(max_length=50,null=True)
    tlf=models.ForeignKey(Phone,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
""" 
"""    
#ManyToMany
class Video(models.Model):
    vidname=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.vidname
class Mouchahed(models.Model):
    name=models.CharField(max_length=50,null=True)
    vid=models.ManyToManyField(Video,null=True)
    def __str__(self):
        return self.name
"""
class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.username
    def createUser():
        return "Hello User"



