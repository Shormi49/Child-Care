
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect






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
