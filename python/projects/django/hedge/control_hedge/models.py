# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.IntegerField()


class SymbolConfig(models.Model):
    symbol = models.CharField(max_length=16, default="")
    amount = models.CharField(max_length=16, default="")
    price = models.CharField(max_length=16, default="")
    askPrice = models.FloatField(default=1)
    bidPrice = models.FloatField(default=1)
    bidAmount = models.FloatField(default=1)
    askAmount = models.FloatField(default=1)
    minAmount = models.FloatField(default=0)
    maxAmount = models.FloatField(default=0)
    dealMaxAmount = models.FloatField(default=0)
    dealProportion = models.FloatField(default=0)
    dealWarningAmount = models.FloatField(default=0)
    status = models.IntegerField(default=1)
    depthStep = models.IntegerField(default=30)


class ApiInfo(models.Model):
    name = models.CharField(max_length=32, default="")
    exchangeName = models.CharField(max_length=16, default="")
    account = models.CharField(max_length=32, default="")
    tag = models.CharField(max_length=126, default="")
    apiKey = models.CharField(max_length=64, default="")
    secretKey = models.CharField(max_length=64, default="")
    jcUid = models.CharField(max_length=16, default="")


class OrderInfo(models.Model):
    jc_order_id = models.CharField(max_length=48)
    symbol = models.CharField(max_length=36)
    base_symbol = models.CharField(max_length=18)
    quote_symbol = models.CharField(max_length=18)
    price = models.DecimalField(max_digits=32, decimal_places=18)
    volume = models.DecimalField(max_digits=32, decimal_places=18)
    side = models.CharField(max_length=8)
    jc_ctime = models.CharField(max_length=13)
    jc_cdate = models.CharField(max_length=36)
    ome_name = models.CharField(max_length=36)
    ome_order_id = models.CharField(max_length=48, blank=True, null=True)
    ome_price = models.DecimalField(max_digits=32, decimal_places=18, blank=True, null=True)
    ome_deal_price = models.DecimalField(max_digits=32, decimal_places=18, blank=True, null=True)
    ome_deal_volume = models.DecimalField(max_digits=32, decimal_places=18, blank=True, null=True)
    ome_volume = models.DecimalField(max_digits=32, decimal_places=18, blank=True, null=True)
    fee = models.DecimalField(max_digits=32, decimal_places=18, blank=True, null=True)
    ome_ctime = models.CharField(max_length=36)
    ome_mtime = models.CharField(max_length=36)
    status = models.CharField(max_length=2)
    ctime = models.CharField(max_length=36)
    mtime = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'order_info'
        unique_together = (('jc_order_id', 'symbol'),)

