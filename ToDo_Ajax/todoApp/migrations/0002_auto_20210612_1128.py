# Generated by Django 3.2.3 on 2021-06-12 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Address',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
