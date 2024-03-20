from django.db import models

# Create your models here.
gender_choice = (("M","M"),("F","F"),)

class Customer_Table(models.Model):
    First_name = models.CharField(max_length = 15)
    Last_name = models.CharField(max_length = 15)
    Gender = models.CharField(max_length = 1, choices= gender_choice)
    Phone_number = models.IntegerField()
    Time = models.TimeField(auto_now_add = True, null = True)

    def __str__(self):
        return f"{self.First_name} {self.Last_name}"

    
class Menu_lemon(models.Model):
    name = models.CharField(max_length = 40)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.price}'