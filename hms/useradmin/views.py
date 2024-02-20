from django.shortcuts import render

def adminlogin(request):
    return render(request, 'admin/adminlogin.html')
