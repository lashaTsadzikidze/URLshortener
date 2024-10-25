from django.shortcuts import render, redirect
from .models import URL
from .helper import generate_short_url

# Create your views here.
def index(request):
    urls = URL.objects.all()
    return render(request, 'index.html', {'urls': urls})

def add_url(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        short_url = generate_short_url()

        new_url = URL.objects.create(long_url=long_url, short_url=short_url)
        new_url.save()

        return render(request, 'shortened.html', {'short_url': short_url})

    return render(request, 'add_url.html')

def redirect_to_short_url(request, short_url):
    return render(request, 'short_url.html', {'short_url': short_url})