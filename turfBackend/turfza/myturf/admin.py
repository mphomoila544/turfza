from django.contrib import admin
from .models import Detail, OwnerShipProof, AccommodationPicture, Rule
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Detail)
admin.site.register(OwnerShipProof)
admin.site.register(AccommodationPicture)
admin.site.register(Rule)
# admin.site.register(User)
