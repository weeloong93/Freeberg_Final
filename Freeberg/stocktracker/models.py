from django.db import models

# Create your models here.

class Stock(models.Model):
    company_name = models.CharField(max_length = 100)
    ticker = models.CharField(max_length=10)
    bloom_ticker = models.CharField(max_length=10, null=True)
    lastprice = models.CharField(max_length = 10000000, default ='-')
    a_gain = models.CharField(max_length=10000000, default='-')
    peg = models.CharField(max_length=1000, default='-')
    revenue = models.CharField(max_length=100000, default='-')
    volume = models.IntegerField(blank=True, default = 1)
    description = models.TextField(null=True)
    start_date = models.DateField(null=True)
    price_change = models.FloatField(blank=True, default = 1)
    market_cap = models.CharField(max_length=100,blank=True, default = 1)
    get_high = models.CharField(max_length=100,blank=True, default = 1)
    get_low = models.CharField(max_length=100,blank=True, default = 1)
    pb_ratio = models.CharField(max_length=100,blank=True, default = 1)
    pe_ratio = models.CharField(max_length=100,blank=True, default = 1)
    dividend = models.CharField(max_length=100,blank=True, default = 1)
    industry = models.CharField(max_length=20, blank=True, default = '-')

    def __str__(self):
        return self.ticker

