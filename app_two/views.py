from django.shortcuts import render, get_object_or_404
from .models import Watch

def index(request):
    watches = Watch.objects.all()
    context = {
        'watches': watches
    }
    return render(request, 'app_two/index.html', context)
