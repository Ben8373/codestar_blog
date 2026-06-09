from django.shortcuts import render, redirect
from django.contrib import messages
from aboutapp.models import About
from blog.forms import CollaborateForm

def about_me(request):
    about = About.objects.all().order_by('-updated_on').first()

    if request.method == "POST":
        form = CollaborateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks — I'll be in touch soon!")
            return redirect("about")
    else:
        form = CollaborateForm()

    return render(request, "aboutapp/about.html", {
        "about": about,
        "collaborate_form": form
    })

def collaborate(request):
    form = CollaborateForm()

    if request.method == "POST":
        form = CollaborateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks — I'll be in touch soon!")
            return redirect("collaborate")

    return render(request, "aboutapp/collaborate.html", {
        "form": form
    })
