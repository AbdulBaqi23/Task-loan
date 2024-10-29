from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class organization(models.Model):
    name = models.CharField(max_length=200)
    amount = models.IntegerField(null=False)
    
    def __str__(self):
        return self.name

class loan(models.Model):
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False,default=0)
    taken_from = models.ForeignKey(organization, on_delete=models.PROTECT)
    time = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return (f'PKR.{self.amount}/- are requested by Mr.{self.requested_by}')