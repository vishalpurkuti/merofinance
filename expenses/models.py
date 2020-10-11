from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from account.models import Account

# Create your models here.


class ExpensesCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='Expenses Category')
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = 'expensescategory'


class Expenses(models.Model):
    title = models.CharField(max_length=100, verbose_name='Expenses Title')
    date = models.DateField(verbose_name='Expenses Date')
    amount = models.FloatField()
    bill = models.ImageField(upload_to='bill/', null=True, blank=True)
    expenses_category = models.ForeignKey(ExpensesCategory, on_delete=CASCADE)

    class Meta:
        db_table = 'expenses'
