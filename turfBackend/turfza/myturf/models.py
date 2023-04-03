from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Detail(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)

    owner = models.CharField(max_length=100)
    nameOfPlace = models.CharField(max_length=200)
    totalNoOfSpace = models.IntegerField()
    location = models.CharField(max_length=50)


class OwnerShipProof(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    img = models.ImageField(upload_to='proof/images', null=True, blank=False)
    idPic = models.ImageField(upload_to='proof/images', null=True, blank=False)
    proofOfResidence = models.ImageField(
        upload_to='proof/images', null=True, blank=False)


class AccommodationPicture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='proof/images/accommodation')


class Rule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rule = models.CharField(max_length=300)


# class Rule(models.Model):
    #rules = ArrayField(ArrayField(models.CharField()))
