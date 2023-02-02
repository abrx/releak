from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'releak/releases.html')

def about(request):
    return HttpResponse('<h1>https://github.com/abrx/releak</h1>')
