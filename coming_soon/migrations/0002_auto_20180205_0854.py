# Generated by Django 2.0.2 on 2018-02-05 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coming_soon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query_users',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='query_users',
            name='mob',
            field=models.CharField(max_length=100),
        ),
    ]