from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models.add_asset import Asset
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


@admin.action(description='Mark selected CCIT Assets as available')
def make_available(modeladmin, request, queryset):
    queryset.update(available_to_borrow=True)


@admin.action(description='Edit selected CCIT Asset')
def edit_selected_assets(modeladmin, request, queryset):
    # Redirect to the edit page for the first selected asset
    # If multiple assets are selected, the user will be prompted to select one.
    if len(queryset) == 1:
        asset_id = queryset.values_list('id', flat=True).first()
        url = reverse('admin:management_asset_change', args=[asset_id])
        return redirect(url)
    else:
        modeladmin.message_user(request, "Please select only one asset to edit.")


class AdminAsset(admin.ModelAdmin):
    list_display = ['asset_id', 'resource_asset_number', 'model', 'purchase_date']
    list_filter = ['purchase_date', 'manufacturer']

    actions = [make_available, edit_selected_assets]


@admin.action(description='Edit selected group')
def edit_selected_group(modeladmin, request, queryset):
    # Redirect to the edit page for the first selected asset
    # If multiple assets are selected, the user will be prompted to select one.
    if len(queryset) == 1:
        group_id = queryset.values_list('id', flat=True).first()
        url = reverse('admin:management_asset_change', args=[group_id])
        return redirect(url)
    else:
        modeladmin.message_user(request, "Please select only one group to edit.")


@admin.action(description='Edit selected user')
def edit_selected_user(modeladmin, request, queryset):
    # Redirect to the edit page for the first selected asset
    # If multiple assets are selected, the user will be prompted to select one.
    if len(queryset) == 1:
        user_id = queryset.values_list('id', flat=True).first()
        url = reverse('admin:management_asset_change', args=[user_id])
        return redirect(url)
    else:
        modeladmin.message_user(request, "Please select only one user to edit.")

class AdminGroup(admin.ModelAdmin):
    actions = [edit_selected_group]

class AdminUser(admin.ModelAdmin):
    actions = [edit_selected_user]

# Register your models here.
admin.site.register(Asset, AdminAsset)
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Group, AdminGroup)
admin.site.register(User, AdminUser)