
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect






@login_required
def add_Child(request):
    if request.method == "POST":
        form = ChildForm(request.POST, request.FILES)
        if form.is_valid():
            child = form.save(commit)
            child.user = request.user
            child.save()
            return render("success")
    else:
        form = childForm()
    return render(request, "main/add_child.html", {"form": form})


vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv