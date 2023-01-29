from django.contrib import admin
from .models.add_device import Device
from .models.add_category import Category
from .models.add_brand import Brand
from .models.add_model import Category_Brand

class AdminDevice(admin.ModelAdmin):
    list_display = ['resource_asset_number', 'purchase_date', 'model', 'color', 'description']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminBrand(admin.ModelAdmin):
        list_display = ['name']

class AdminCategory_Brand(admin.ModelAdmin):
        list_display = ['name', 'category', 'brand']

# Register your models here.
admin.site.register(Device, AdminDevice)
admin.site.register(Category, AdminCategory)
admin.site.register(Brand, AdminBrand)
admin.site.register(Category_Brand, AdminCategory_Brand)