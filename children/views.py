# from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import  ChildForm
from .models import  Child

from django.shortcuts import redirect

from django.contrib import messages



@login_required
def add_child(request):
    if request.method == "POST":
        form = ChildForm(request.POST, request.FILES)
        if form.is_valid():
            child = form.save(commit=False)
            child.user = request.user
            child.save()
            return redirect("success")
    else:
        form = ChildForm()
    return render(request, "main/add_child.html", {"form": form})






def success(request):
    return render(request, "main/success.html")





def children(request):
    user = request.user
    children = user.children.all()
    return render(request, "main/children.html", {"children": children})
