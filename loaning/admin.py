from django.contrib import admin
from .models.resource_signout_log import Log
from .models.signatures import Signature

class AdminLog(admin.ModelAdmin):
    list_display = ['asset_ID', 'resource_asset_number']

class AdminSignature(admin.ModelAdmin):
    list_display = ['signature']

# Register your models here.
admin.site.register(Log, AdminLog)
admin.site.register(Signature, AdminSignature)