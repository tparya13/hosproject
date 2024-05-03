from django.db import models
# Create your models here.
class Homes(models.Model):
    name=models.CharField(max_length=280)
    image=models.ImageField(upload_to='homes',null=True,blank=True)
    class Meta:
        ordering=('name',)
    def __str__(self):
        return self.name

class Testi(models.Model):
    name=models.CharField(max_length=60)
    detail=models.CharField(max_length=280)
    place=models.CharField(max_length=150)    
    def __str__(self):
        return self.name

class Enquery(models.Model):
    names=models.CharField(max_length=280)
    email=models.CharField(max_length=280)
    number=models.IntegerField(unique=True)
    message=models.CharField(max_length=350)     
    def __str__(self):
        return self.names

class Appointment(models.Model):
    name=models.CharField(max_length=250)
    email=models.CharField(max_length=150)
    phone=models.IntegerField(unique=True)
    date=models.CharField(max_length=15)
    time=models.CharField(max_length=15)
    age=models.IntegerField()
    gender=models.CharField(max_length=60)
    address=models.CharField(max_length=300)
    message=models.CharField(max_length=280)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name=models.CharField(max_length=250)
    email=models.CharField(max_length=150)
    phone=models.IntegerField(unique=True)
    subject=models.CharField(max_length=250)
    message=models.CharField(max_length=280)
    def __str__(self):
        return self.name

class Branch(models.Model):
    image=models.ImageField(upload_to='branch')
    name=models.CharField(max_length=280,unique=True)
    class Meta:
        ordering=('name',)
    def __str__(self):
        return self.name

class Gallery(models.Model):
    image=models.ImageField(upload_to='gallerys',blank=True)
    class Meta:
        ordering=('image',) 
    def ImageField(self):
        return self.image

class Blog(models.Model):
    image=models.ImageField(upload_to='blog')
    name=models.CharField(max_length=280,unique=True)
    class Meta:
        ordering=('name',) 
    def __str__(self):
        return self.name
class Package(models.Model):
    image=models.ImageField(upload_to='package')
    price=models.IntegerField()
    cont1=models.CharField(max_length=300)
    cont2=models.CharField(max_length=300)
    cont3=models.CharField(max_length=300)
    cont4=models.CharField(max_length=300)
    cont5=models.CharField(max_length=300)
    cont6=models.CharField(max_length=300)
    cont7=models.CharField(max_length=300,blank=True)
    cont8=models.CharField(max_length=300,blank=True)
    cont9=models.CharField(max_length=300,blank=True)
    cont10=models.CharField(max_length=300,blank=True)
    cont11=models.CharField(max_length=300,blank=True)
    cont12=models.CharField(max_length=300,blank=True)
    cont13=models.CharField(max_length=300  ,blank=True)
    name=models.CharField(max_length=250,unique=True)
    class Meta:
        ordering=('name',)   
    def __str__(self):
        return self.name    
