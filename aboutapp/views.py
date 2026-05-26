from django.shortcuts import render

from aboutapp.models import About


def about_view(request):
    about = About.objects.all().order_by('-updated_on').first()
    return render(request, 'aboutapp/about.html', {'about': about})
