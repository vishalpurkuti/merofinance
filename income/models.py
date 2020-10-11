from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.files import ImageField
from account.models import Account
# Create your models here.


class IncomeCategory(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(Account, on_delete=CASCADE)


class Income(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    amount = models.FloatField()
    receipt = models.ImageField(upload_to='receipt/', null=True, blank=True)
    income_category = models.ForeignKey(IncomeCategory, on_delete=CASCADE)
