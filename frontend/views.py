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
import requests
import xml.etree.ElementTree as ET

# Create your views here.
@login_required(login_url='accounts:login')
def index(request):
    logs = Log.objects.filter(returned=False).order_by('-sign_out_date')[:5]
    assets = Asset.objects.filter(available_to_borrow=True)
    return render(request, 'frontend/index.html', {'logs': logs, 'assets': assets})


@login_required(login_url='accounts:login')
def showDevice(request):
    # get id
    device_id = int(request.GET.get('device_id'))

    # get content
    url = f'https://datasafely.online.miradore.com/API/' \
          f'Device/{device_id}?auth=2_Fy5AU84,9xbi]6C&select=*,ReportedLocation.*,Location.*,InvDevice.*,' \
          f'Tag.Name,User.Email,User.LastName,User.FirstName' \
          f'&filters=InvDevice.InventoryTime%20gt%20%2724.06.2014%27&options=dateFormat=dd.MM.yyyy'
    response = requests.get(url)
    xml_content = response.content

    # parse XML content
    root = ET.fromstring(xml_content)

    # collect information from Miradore
    software = root.find('Items/Device/InvDevice/SoftwareVersion')
    serial = root.find('Items/Device/InvDevice/SerialNumber')
    status = root.find('Items/Device/OnlineStatus')
    location = root.find('Items/Device/Location/FullName')
    last_reported = root.find('Items/Device/LastReported')
    latitude = root.find('Items/Device/ReportedLocation/Latitude')
    longitude = root.find('Items/Device/ReportedLocation/Longitude')

    # collect information from database
    asset = Asset.objects.get(asset_id=device_id)

    # pass information
    context = {
        'id': device_id,
        'resource_asset_number': asset.resource_asset_number,
        'model': asset.model,
        'manufacturer': asset.manufacturer,
        'software': software.text if software is not None else '',
        'serial': serial.text if serial is not None else '',
        'status': status.text if status is not None else 'Inactive',
        'location': location.text if location is not None else 'Unavailable',
        'last_reported': last_reported.text if last_reported is not None else 'Unavailable',
        'latitude': float(latitude.text) if latitude is not None else '',
        'longitude': float(longitude.text) if longitude is not None else '',
    }

    # render the content in a template
    return render(request, "frontend/device.html", context)


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

