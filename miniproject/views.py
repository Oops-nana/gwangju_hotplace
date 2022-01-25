from django.shortcuts import render

def maps(request):
    return render(request, 'miniproject/maps.html')

def test(request):
    return render(request, 'miniproject/test.html')