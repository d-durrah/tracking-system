from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from loaning.models.resource_signout_log import Log
from management.models import Asset
from loaning.models.signatures import Signature


# Create your views here.
@login_required(login_url='accounts:login')
def index(request):
    return render(request, 'frontend/index.html')


@login_required(login_url='accounts:login')
def generatePDF(request):
    log_id = int(request.GET.get('log'))
    log = Log.objects.get(id=log_id)
    context = {
        'log_id': log_id,
        'ID_number': log.ID_number,
        'asset_ID': log.asset_ID,
        'resource_asset_number': log.resource_asset_number,
        'item_description': log.model,
        'purpose': log.purpose,
        'borrow_date': log.borrow_date,
        'return_date': log.return_date,
    }

    return render(request, 'frontend/view_submission.html', context)


@login_required(login_url='accounts:login')
def showCurrent(request):
    logs = Log.objects.filter(returned=False).order_by('-borrow_date')
    return render(request, 'frontend/current_loans.html', {'logs': logs})


@login_required(login_url='accounts:login')
def showAvailable(request):
    assets = Asset.objects.filter(available_to_borrow=True)
    return render(request, 'frontend/assets_available.html', {'assets': assets})

