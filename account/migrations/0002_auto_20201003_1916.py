# Generated by Django 3.0.2 on 2020-10-03 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='profile_imge',
            new_name='profile_image',
        ),
    ]
