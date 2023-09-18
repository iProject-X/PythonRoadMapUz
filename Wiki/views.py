from django.shortcuts import render,redirect
from Wiki.models import Language, Child

# Create your views here.

def home(request):


    return render(request, 'index.html', )

def second(request):
    return render(request, 'docs-page.html')