# Generated by Django 3.1.2 on 2023-02-09 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myturf', '0008_auto_20230209_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownershipproof',
            name='proofOfResidence',
            field=models.FileField(blank=True, upload_to='proof/documents'),
        ),
    ]