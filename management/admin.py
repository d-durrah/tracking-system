from django.contrib import admin
from .models.add_asset import Asset
from .models.add_category import Category
from .models.add_supplier import Supplier
from .models.add_device import Device


class AdminAsset(admin.ModelAdmin):
    list_display = ['resource_asset_number', 'purchase_date', 'supplier', 'color', 'description']
    list_filter = ['purchase_date', 'supplier', 'category', 'color']


class AdminCategory(admin.ModelAdmin):
    list_display = ['category']


class AdminSupplier(admin.ModelAdmin):
    list_display = ['supplier']


class AdminDevice(admin.ModelAdmin):
    list_display = ['name', 'supplier', 'category']
    list_filter = ['supplier', 'category']


# Register your models here.
admin.site.register(Asset, AdminAsset)
admin.site.register(Supplier, AdminSupplier)
admin.site.register(Category, AdminCategory)
admin.site.register(Device, AdminDevice)
