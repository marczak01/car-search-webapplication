from django.contrib import admin
from .models import Profile, Advert, Fuel, Brand, PriceReminderConnection
# Register your models here.

admin.site.register(Profile)
admin.site.register(Advert)
admin.site.register(Fuel)
admin.site.register(Brand)
admin.site.register(PriceReminderConnection)
