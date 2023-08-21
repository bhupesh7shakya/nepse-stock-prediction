from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    ltp = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.symbol
    
class PriceHistory(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    open_price = models.DecimalField(max_digits=10, decimal_places=2)
    close_price = models.DecimalField(max_digits=10, decimal_places=2)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.IntegerField()
    change = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.company.symbol} - {self.company.name} Price History"
    
class Announcement(models.Model):
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class News(models.Model):
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Fund(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"Fund of {self.user.username}"
    
class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"Payment of {self.user.username}"
    
class Purchase(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    qty = models.IntegerField()
    buy_price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"Purchase of {self.qty} {self.company.symbol} by {self.user.username}"
    
class Sold(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    qty = models.IntegerField()
    sold_price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"Sold {self.qty} {self.company.symbol} by {self.user.username}"
