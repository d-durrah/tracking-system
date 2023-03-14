from django.contrib import admin
from .models.resource_signout_log import Log
from .models.signatures import Signature
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.urls import path


class AdminLog(admin.ModelAdmin):
    list_display = ['id', 'asset_ID', 'resource_asset_number', 'borrow_date', 'return_date', 'returned']
    list_filter = ['asset_ID', 'borrow_date', 'return_date', 'returned']


class AdminSignature(admin.ModelAdmin):
    list_display = ['signature', 'log_id']

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('<int:pk>/view-pdf/', self.view_pdf, name='view_pdf'),
        ]
        return my_urls + urls

    def view_pdf(self, request, pk):
        signature = get_object_or_404(Signature, pk=pk)
        response = FileResponse(open(signature.pdf_file.path, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{signature.pdf_file.name}"'
        return response


# Register your models here.
admin.site.register(Log, AdminLog)
admin.site.register(Signature, AdminSignature)
