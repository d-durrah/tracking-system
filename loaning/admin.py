from django.contrib import admin
from .models.resource_signout_log import Log
from .models.signatures import Signature
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.urls import path
from django.shortcuts import redirect
from django.urls import reverse

@admin.action(description='Edit selected Resource Sign-out Log')
def edit_selected_log(modeladmin, request, queryset):
    # Redirect to the edit page for the first selected asset
    # If multiple assets are selected, the user will be prompted to select one.
    if len(queryset) == 1:
        log_id = queryset.values_list('id', flat=True).first()
        url = reverse('admin:loaning_log_change', args=[log_id])
        return redirect(url)
    else:
        modeladmin.message_user(request, "Please select only one log to edit.")

class AdminLog(admin.ModelAdmin):
    list_display = ['id', 'asset_ID', 'resource_asset_number', 'sign_out_date', 'return_date', 'returned']
    list_filter = ['asset_ID', 'sign_out_date', 'return_date', 'returned']
    actions = [edit_selected_log]

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
