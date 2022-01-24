from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, DateField
from django.contrib.auth.models import User

# Create your models here.
class BloodRequestPost(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='articale')
    phone=models.CharField(max_length=20)
    bloodgroup=models.CharField(max_length=20)
    neededBlood=models.CharField(max_length=20)
    locations=models.CharField(max_length=50)
    requestDate=models.DateTimeField(max_length=50)
    currentDate=models.DateTimeField(auto_now_add=True, blank=False)
    update_date=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-currentDate',]

    def __str__(self) -> str:
        return self.author.username
    
