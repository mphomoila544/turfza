# Generated by Django 3.1.2 on 2023-02-08 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myturf', '0003_auto_20230208_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownershipproof',
            name='idPic',
            field=models.ImageField(upload_to='proof'),
        ),
        migrations.AlterField(
            model_name='ownershipproof',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='ownershipproof',
            name='proofOfResidence',
            field=models.FileField(upload_to=''),
        ),
    ]
