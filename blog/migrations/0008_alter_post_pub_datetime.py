# Generated by Django 4.1.7 on 2023-03-12 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_datetime',
            field=models.DateTimeField(verbose_name='Publish Datetime'),
        ),
    ]
