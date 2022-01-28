from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import CommonPlace, museumDetail
from django.forms.models import model_to_dict
from member.models import Member

import miniproject


def maps(request):
    place = CommonPlace.objects.all()
    museumdtl = museumDetail.objects.all()
    
    data = []
    comment_data = []
    user_data = []
    museum_data = []
    for i in place:
        i = model_to_dict(i)
        data.append(i)
    for j in museumdtl:
        j = model_to_dict(j)
        museum_data.append(j)
    return render(request, 'miniproject/maps.html', 
                  {'data': data, 'museum_data': museum_data})


def login_session(request):
    user_pk = request.session.get('id')

    if user_pk:
        fuser = Member.objects.get(pk=user_pk)
    return HttpResponse(fuser)

    # return render(request, 'member/login.html')

def logout(request):
    del request.session['id'] # 개별 삭제
    del request.session['user_name'] # 개별 삭제
    request.session.flush() # 전체 삭제

    return redirect('/member/login')


def index(request):
    return render(request, 'miniproject/index.html')
