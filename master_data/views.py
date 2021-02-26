from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url="login/")
def homepage(request):
    return render(request, 'adminlte/base.html')
