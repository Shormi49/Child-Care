# from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required

from .forms import PackageForm


from django.shortcuts import render, redirect






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
