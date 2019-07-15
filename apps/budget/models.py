from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

class ItemType(models.Model):
    name = models.CharField(max_length=30)

class Item(models.Model):
    bank = models.ForeignKey('Bank', on_delete=models.CASCADE)
    item_type = models.ForeignKey('ItemType', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)


