from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def teamprofile(request):
    return render(request, 'aboutme.html')