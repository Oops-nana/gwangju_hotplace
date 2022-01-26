from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import CommonPlace, museumDetail
from django.forms.models import model_to_dict

import miniproject


def maps(request):
    place = CommonPlace.objects.all()
    data = []
    for i in place:
        i = model_to_dict(i)
        data.append(i)
    return render(request, 'miniproject/maps.html', {'data': data})


def index(request):
    return render(request, 'miniproject/index.html')
