from django.shortcuts import render

def maps(request):
    return render(request, 'miniproject/maps.html')
