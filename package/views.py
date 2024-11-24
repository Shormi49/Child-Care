
from django.contrib.auth.decorators import login_required

from .forms import PackageForm
from .models import Package
from django.contrib.auth import logout
from django.shortcuts import redirect

from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
@login_required
def add_package(request):
    if request.method == "POST":
        form = PackageForm(request.POST)
        if form.is_valid():
            package = form.save()
            package.user = request.user
            package.save()
            return redirect("waiting_for_admin")
    else:
        form = PackageForm()
    return render(request, "#", {"form": form})

def waiting_for_admin(request):
    return render(request, "main/waiting_for_admin.html")