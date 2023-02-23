from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.defaultfilters import urlencode
from django.urls import reverse
from .forms import ResourceSignOutForm
from .models.current_loans import Log
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
            asset = Asset.objects.get(id=r_num.id)

            # get description
            desc = asset.description

            # update asset availability
            # asset.available_to_borrow = False
            # asset.save()

            # save to loan database
            log = Log(
                ID_number=form.cleaned_data['ID_number'],
                resource_asset_number=form.cleaned_data['resource_asset_number'],
                item_description=desc,
                purpose=form.cleaned_data['purpose'],
                borrow_date=form.cleaned_data['borrow_date'],
                return_date=form.cleaned_data['return_date'],
            )
            log.save()

            # send message
            # messages.info(request, 'Upload signature to complete resource sign-out.')

            # redirect to generate pdf page
            # current = log.id
            # print(current)
            return HttpResponseRedirect(reverse("frontend:pdf") + '?' + 'log=' + str(log.id))


    # if a GET (or any other method) we'll create a blank form
    else:
        form = ResourceSignOutForm()

    return render(request, 'frontend/asset_loan_form.html', {'form': form})