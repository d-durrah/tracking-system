from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
            r_num = form.cleaned_data.get('asset_ID')
            asset = Asset.objects.get(id=r_num.id)

            # get resource_asset_number & model
            num = asset.resource_asset_number
            model = asset.model

            # update asset availability
            asset.available_to_borrow = False
            asset.save()

            # save to loan database
            log = Log(
                ID_number=form.cleaned_data['ID_number'],
                asset_ID=form.cleaned_data['asset_ID'],
                resource_asset_number=num,
                model=model,
                purpose=form.cleaned_data['purpose'],
                borrow_date=form.cleaned_data['borrow_date'],
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

    return render(request, 'frontend/submit_signature.html', {'form': form})