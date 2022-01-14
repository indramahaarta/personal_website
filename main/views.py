from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def mainview(request):
    return render(request, 'mainview.html')