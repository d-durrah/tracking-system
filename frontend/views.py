from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from loaning.models import Log

# Create your views here.
@login_required(login_url='accounts:login')
def index(request):
    return render(request, 'frontend/index.html')

@login_required(login_url='accounts:login')
def generatePDF(request):
    log_id = int(request.GET.get('log'))
    log = Current.objects.get(id=log_id)
    context = {
        'ID_number': log.ID_number,
        'resource_asset_number': log.resource_asset_number,
        'item_description': log.item_description,
        'purpose': log.purpose,
        'borrow_date': log.borrow_date,
        'return_date': log.return_date,
    }
    return render(request, 'frontend/view_submission.html', context)



