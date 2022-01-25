from django.shortcuts import render

def maps(request):
    return render(request, 'miniproject/maps.html')

def login(request):
    return render(request, 'miniproject/login.html')
