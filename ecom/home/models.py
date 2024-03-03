from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class ourservice(models.Model):
    name=models.CharField(max_length=100,default="")
    description=models.TextField(default="")


    def __str__(self):
        return self.name
    

class deppp(models.Model):
    name=models.CharField(max_length=100,default="")    

    def __str__(self):
        return self.name
    

class appo(models.Model):
    pname=models.CharField(max_length=100,default="")    
    depp=models.ForeignKey(deppp,on_delete=models.CASCADE)
    email=models.CharField(max_length=100,default="")
    phone=models.CharField(max_length=100,default="")
    date=models.DateTimeField()

    def __str__(self):
        return self.pname
    
    

    
    

class Bloodavailabilty(models.Model):
    name=models.CharField(max_length=100,default="")  
    unit=models.CharField(max_length=100,default="")   

    def __str__(self):
        return self.name
    

class ourdocters(models.Model):
    # name=models.CharField(max_length=100,default="")
    name=models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    # department=models.CharField(max_length=100,default="")
    department=models.ForeignKey(deppp,on_delete=models.CASCADE)
    description=models.TextField(default="")
    position=models.CharField(max_length=100,default="")
    workingtime=models.DateTimeField()
    image=models.ImageField(upload_to='images')


    def __str__(self):
        return self.name.username
    



class field(models.Model):
    name=models.CharField(max_length=100,default="")


    def __str__(self):
        return self.name
    
    



   

    def __str__(self):
        return self.patientname
    

class docters_booking(models.Model):
    pname=models.CharField(max_length=100,default="")
    age=models.IntegerField()
    date=models.DateTimeField()
    phone=models.CharField(max_length=100,default="")
    email=models.CharField(max_length=100,default="")

    def __str__(self):
        return self.pname
    
class articles(models.Model):
    name=models.CharField(max_length=100,default="")
    description=models.TextField()    
    image=models.ImageField(upload_to="images")
   
    def __str__(self):
        return self.name
    
        
    



class Medicine(models.Model):
    name=models.CharField(max_length=100,default="")
    description=models.TextField()

    def __str__(self):
        return self.name
    
# class Docters(models.Model):
#     name=models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
#     # image=models.ImageField(upload_to='images')  

#     def __str__(self):
#         return self.name
      
    
class Patient(models.Model):
    name=models.OneToOneField(User,on_delete=models.CASCADE,unique=True)

    def __str__(self):
        return self.name.username
    
class prescription(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    docter=models.ForeignKey(User,on_delete=models.CASCADE)
    nextdate=models.CharField(max_length=100,default="")
    

    def __str__(self):
        return self.patient.name.username
    


class prescribed(models.Model):
    Prescription=models.ForeignKey(prescription,on_delete=models.CASCADE)
    medicine=models.ForeignKey(Medicine,on_delete=models.CASCADE) 
    time=models.CharField(max_length=100,null=True,blank=True)
    quantity=models.CharField(max_length=100,default="")


    def __str__(self) -> str:
        return self.Prescription.patient.name.username + '' + str(self.Prescription.date)   


    

        
     
    
  
    



