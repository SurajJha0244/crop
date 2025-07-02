from django.contrib import admin

from .models import product,contact,crop_recommend

admin.site.register(product)
admin.site.register(contact)
admin.site.register(crop_recommend)
# Register your models here.
