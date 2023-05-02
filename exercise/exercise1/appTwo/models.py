from django.db import models

# Create your models here.
class users(models.Model):
    id = models.AutoField(primary_key=True)
    firstName=models.CharField(max_length=20,unique=True)
    lastName=models.CharField( max_length=50,unique=True)
    eMail=models.EmailField( max_length=254,unique=True)

    def __str__(self):
        return self.firstName
    
