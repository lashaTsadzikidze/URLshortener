from django.shortcuts import render
from .models import URL
import random
import string

# Create your views here.
def index(request):

    return render(request, 'index.html')