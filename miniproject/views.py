from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse

def maps(request):
    return render(request, 'miniproject/maps.html')


def test(request):
    return render(request, 'miniproject/test.html')
