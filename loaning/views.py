from datetime import date
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ResourceSignOutForm, SignatureForm
from .models.resource_signout_log import Log
from management.models.add_asset import Asset

@login_required(login_url='accounts:login')
def resourceSignOutForm(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = ResourceSignOutForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # get the asset
            r_num = form.cleaned_data.get('resource_asset_number')
            asset = Asset.objects.get(resource_asset_number=r_num)
            # print(asset)

            # get resource_asset_number & model
            a_id = int(asset.asset_id)
            model = asset.model

            # get the user
            u_id = form.cleaned_data.get('employee_ID')
            user = User.objects.get(username=u_id)

            # get name & id
            name = user.first_name+" "+user.last_name
            email = user.email

            # update asset availability
            asset.available_to_borrow = False
            # print("Available to borrow set to False")
            asset.save()

            # save to loan database
            log = Log(
                employee_ID=form.cleaned_data['employee_ID'],
                name=name,
                email=email,
                resource_asset_number=form.cleaned_data['resource_asset_number'],
                asset_ID=a_id,
                model=model,
                purpose=form.cleaned_data['purpose'],
                sign_out_date=form.cleaned_data['sign_out_date'],
                return_date=form.cleaned_data['return_date'],
                returned=False,
            )
            log.save()

            # redirect to generate pdf page
            return HttpResponseRedirect(reverse("frontend:pdf") + '?' + 'log=' + str(log.id))


    # if a GET (or any other method) we'll create a blank form
    else:
        form = ResourceSignOutForm()

    return render(request, 'frontend/asset_loan_form.html', {'form': form})

@login_required(login_url='accounts:login')
def signatureForm(request):
    log_id = request.GET.get('log')

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = SignatureForm(request.POST, request.FILES)
        # print("Start...")

        # check whether it's valid:
        if form.is_valid():
            # save to signature database along with log_id
            form.save()

            # send message
            messages.info(request, 'Resource sign-out completed successfully.')

            # redirect to index page
            return redirect("frontend:index")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignatureForm(initial={'log_id': request.GET.get('log')})

    return render(request, 'frontend/submit_signature.html', {'form': form, 'log_id': log_id})
@login_required(login_url='accounts:login')
def returnAsset(request):
    # get log record
    num = request.POST.get('asset')
    log = Log.objects.get(pk=num)

    # add return date
    log.returned = True
    log.returned_on = date.today()
    log.save()

    # make asset available to borrow
    asset = Asset.objects.get(asset_id=log.asset_ID)
    asset.available_to_borrow = True
    asset.save()

    # send message
    messages.info(request, f'Asset ID {log.asset_ID} has been returned.')

    # redirect to index page
    return redirect("frontend:index")
