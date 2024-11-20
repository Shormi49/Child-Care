from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile
from .forms import UserRegistrationForm


def user_logout(request):
    logout(request)
    return redirect("home")#logout

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(
                user=user,
                address=form.cleaned_data["address"],
                contact=form.cleaned_data["contact"],
            )
            login(request, user)
            return redirect("home")
    else:
        form = UserRegistrationForm()
    return render(request, "main/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "main/login.html", {"form": form})
