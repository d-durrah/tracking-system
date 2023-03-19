from django.contrib import admin
from .models.add_asset import Asset

class AdminAsset(admin.ModelAdmin):
    list_display = ['asset_id', 'resource_asset_number', 'model', 'purchase_date']
    list_filter = ['purchase_date', 'manufacturer']


# Register your models here.
admin.site.register(Asset, AdminAsset)