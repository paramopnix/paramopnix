from django.db import models

# Deposit class
class Deposit(models.Model):
    amount = models.DecimalField(max_digit = 10, decimal_places = 2)
    date = models.DateTimeField(auto_now_add=True)
    
# Payment receiving class
class Payment(models.Model):
    amount = models.DecimalField() 
    date = models.DateTimeField(auto_now_add = True)
    
    
