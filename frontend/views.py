from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render
from django.contrib import messages
from loaning.models.resource_signout_log import Log
from management.models import Asset
from loaning.models.signatures import Signature
from loaning.forms import SignatureForm
from loaning.models import Log
from management.models import Asset


# Create your views here.
@login_required(login_url='accounts:login')
def index(request):
    logs = Log.objects.filter(returned=False).order_by('-sign_out_date')[:5]
    assets = Asset.objects.filter(available_to_borrow=True)
    return render(request, 'frontend/index.html', {'logs': logs, 'assets': assets})



@login_required(login_url='accounts:login')
def generatePDF(request):
    log_id = int(request.GET.get('log'))
    log = Log.objects.get(id=log_id)
    context = {
        'log_id': log_id,
        'employee_ID': log.employee_ID,
        'name': log.name,
        'email': log.email,
        'asset_ID': log.asset_ID,
        'resource_asset_number': log.resource_asset_number,
        'item_description': log.model,
        'purpose': log.purpose,
        'sign_out_date': log.sign_out_date,
        'return_date': log.return_date,
    }

    return render(request, 'frontend/view_submission.html', context)

@login_required(login_url='accounts:login')
def cancelSignOut(request):
    log_id = int(request.GET.get('log'))
    log = Log.objects.get(id=log_id)

    # turn asset available to borrow
    asset = Asset.objects.get(asset_id=log.asset_ID)
    asset.available_to_borrow = True
    asset.save()

    # delete log
    log.delete()

    # send message
    messages.info(request, 'Form submission cancelled.')

    return redirect("frontend:index")

@login_required(login_url='accounts:login')
def showCurrent(request):
    logs = Log.objects.filter(returned=False).order_by('-sign_out_date')
    return render(request, 'frontend/current_loans.html', {'logs': logs})


@login_required(login_url='accounts:login')
def showAvailable(request):
    assets = Asset.objects.filter(available_to_borrow=True)
    return render(request, 'frontend/assets_available.html', {'assets': assets})

