from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.shortcuts import render, redirect
from loaning.models.signatures import Signature
from loaning.models.resource_signout_log import Log
from loaning.forms import SignatureForm

# Create your views here.
@login_required(login_url='accounts:login')
def index(request):
    return render(request, 'frontend/index.html')

@login_required(login_url='accounts:login')
def generatePDF(request):
    log_id = int(request.GET.get('log'))
    log = Log.objects.get(id=log_id)
    context = {
        'ID_number': log.ID_number,
        'asset_ID': log.asset_ID,
        'resource_asset_number': log.resource_asset_number,
        'item_description': log.model,
        'purpose': log.purpose,
        'borrow_date': log.borrow_date,
        'return_date': log.return_date,
    }

    return render(request, 'frontend/view_submission.html', context)
