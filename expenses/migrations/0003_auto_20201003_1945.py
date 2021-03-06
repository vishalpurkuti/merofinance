# Generated by Django 3.0.2 on 2020-10-03 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_expenses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='bill',
            field=models.ImageField(blank=True, null=True, upload_to='bill/'),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(verbose_name='Expenses Date'),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Expenses Title'),
        ),
        migrations.AlterField(
            model_name='expensescategory',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Expenses Category'),
        ),
    ]
