from django.db import models

class MissingPerson(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    missing_date=models.DateField()
    last_seen_Location=models.CharField(max_length=300)
    contact_info=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='missing_photos/',blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    aadhar_number=models.CharField(max_length=12,blank=True,null=True)

    def __str__(self):
        return self.name
    
    

# Create your models here.
