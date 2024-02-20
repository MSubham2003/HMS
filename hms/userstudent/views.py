from django.shortcuts import render

def studentlogin(request):
    return render(request, 'signin.html')

def studentregister(request):
    return render(request, 'registration.html')
