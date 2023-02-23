from django.contrib import admin
from .models.current_loans import Log
from .models.loan_history import Logg

class AdminLog(admin.ModelAdmin):
    list_display = ['resource_asset_number', 'item_description', 'purpose']

# Register your models here.
admin.site.register(Logg, AdminLog)
admin.site.register(Log, AdminLog)