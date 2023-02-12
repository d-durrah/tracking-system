from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ResourceSignOutForm
from .models.current_loans import Current
from management.models.add_asset import Asset


def get_asset(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = ResourceSignOutForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # update asset availability
            r_num = form.cleaned_data.get('resource_asset_number')
            asset = Asset.objects.get(id=r_num.id)
            asset.available_to_borrow = False
            asset.save()

            # create a log
            form.save()

            # save to current loans database
            current = Current(
                resource_asset_number=form.cleaned_data['resource_asset_number'],
                item_description=form.cleaned_data['item_description'],
                purpose=form.cleaned_data['purpose'],
                ID_number=form.cleaned_data['ID_number'],
                borrow_date=form.cleaned_data['borrow_date'],
            )
            current.save()

            # send message
            messages.success(request, 'Resource sign-off was successful.')

            # redirect to index
            return redirect('frontend:index')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ResourceSignOutForm()

    return render(request, 'frontend/asset_loan_form.html', {'form': form})