# Generated by Django 3.1.2 on 2023-02-12 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myturf', '0011_auto_20230209_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownershipproof',
            name='proofOfResidence',
            field=models.ImageField(null=True, upload_to='proof/images'),
        ),
    ]
