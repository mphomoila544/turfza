# Generated by Django 3.1.2 on 2023-02-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myturf', '0010_auto_20230209_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownershipproof',
            name='img',
            field=models.ImageField(null=True, upload_to='proof/images'),
        ),
    ]
