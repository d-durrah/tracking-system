from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='accounts:login')
def home(request):
    return render(request, 'user_manual/home.html')


@login_required(login_url='accounts:login')
def ios_manual(request):
    return render(request, 'user_manual/apple.html')


@login_required(login_url='accounts:login')
def android_manual(request):
    return render(request, 'user_manual/android-manual-page.html')


@login_required(login_url='accounts:login')
def windows_manual(request):
    return render(request, 'user_manual/windows-manual-page.html')
