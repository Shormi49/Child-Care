# from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from .models import Donation

def make_donation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact_number = request.POST.get('contact_number')
        transaction_id = request.POST.get('transaction_id')

        if name and contact_number and transaction_id:
            # Save donation details to the database
            Donation.objects.create(
                name=name,
                contact_number=contact_number,
                transaction_id=transaction_id
            )
            messages.success(request, "Thank you for your donation!")
            return redirect('thank_you')
        else:
            messages.error(request, "Please fill in all fields.")

    return render(request, 'main/donation_form.html')  # Render the donation form template

def thank_you(request):
    return render(request, 'main/thank_you.html')  # Render the thank-you template



def user_logout(request):
    logout(request)
    return redirect("home")


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


@login_required
def control_panel(request):
    return render(request, "main/control_panel.html")
















