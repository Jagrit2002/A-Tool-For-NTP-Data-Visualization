from django.db import models

# Create your models here.

class New(models.Model):
    pc_time = models.CharField(null =True , blank = True , max_length=200)
    date = models.CharField(null =True , blank = True , max_length=200)
    ntpserverip = models.CharField(blank=True, null=True , max_length=200)
    stratum = models.BigIntegerField(blank=True, null=True)
    pcip = models.CharField(blank=True, null=True , max_length =2)
    t0 = models.DecimalField(max_digits=250 , decimal_places=10 , blank = True , null = True)
    t1 = models.DecimalField(max_digits=250 , decimal_places=10 , blank = True , null = True)
    t2 = models.DecimalField(max_digits=250 , decimal_places=10 , blank = True , null = True)
    t3 = models.DecimalField(max_digits=250 , decimal_places=10 , blank = True , null = True)
    toffset = models.DecimalField(max_digits=25 , decimal_places=10 , blank = True , null = True)
    tdelay = models.DecimalField(max_digits=25 , decimal_places=10  , blank=True , null = True)
    iserror = models.CharField(blank=True, null=True , max_length=200)
    errmsg =models.CharField(blank=True, null=True , max_length=200)
class N(models.Model):
    pc_time = models.CharField(null =True , blank = True , max_length=200)
    date = models.CharField(null =True , blank = True , max_length=200)
    ntpserverip = models.CharField(blank=True, null=True , max_length=200)
    stratum = models.BigIntegerField(blank=True, null=True)
    pcip = models.CharField(blank=True, null=True , max_length =2)
    t0 = models.DecimalField(max_digits=250 , decimal_places=0 , blank = True , null = True)
    t1 = models.DecimalField(max_digits=250 , decimal_places=0 , blank = True , null = True)
    t2 = models.DecimalField(max_digits=250 , decimal_places=0 , blank = True , null = True)
    t3 = models.DecimalField(max_digits=250 , decimal_places=0 , blank = True , null = True)
    toffset = models.DecimalField(max_digits=25 , decimal_places=10 , blank = True , null = True)
    tdelay = models.DecimalField(max_digits=25 , decimal_places=10  , blank=True , null = True)
    iserror = models.CharField(blank=True, null=True , max_length=200)
    errmsg =models.CharField(blank=True, null=True , max_length=200)

   
