from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    ltp = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.symbol
    
class PriceHistory(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name="price_histories")
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
    company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name="announcements")

    def __str__(self):
        return self.title
    
class News(models.Model):
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name="news")
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
    

class Order(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    ORDER_TYPES = (
        ('buy', 'Buy Order'),
        ('sell', 'Sell Order'),
    )

    order_type=models.CharField(max_length=10,choices=ORDER_TYPES)
    PENDING_STATUS='P'
    COMPLETE_STATUS='C'
    STATUS=(
        (PENDING_STATUS,'Pending'),
        (COMPLETE_STATUS,"Complete"),
    )
    status=models.CharField(max_length=10,choices=STATUS,default=PENDING_STATUS)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sold {self.qty} {self.company.symbol} by {self.user.username}"
    
    


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('buy', 'Buy Order'),
        ('sell', 'Sell Order'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=10,choices=TRANSACTION_TYPES)


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Portfolio - {self.company.name}"