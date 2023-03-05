from django.contrib import admin
from .models.add_asset import Asset

class AdminAsset(admin.ModelAdmin):
    list_display = ['asset_id', 'model']
    # list_filter = ['purchase_date', 'supplier', 'category', 'color']


# Register your models here.
admin.site.register(Asset, AdminAsset)