from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from member.models import Member

import miniproject


def maps(request):
    return render(request, 'miniproject/maps.html')

def login_session(request):
    user_pk = request.session.get('user_id')

    if user_pk:
        fuser = Member.objects.get(pk=user_pk)
    return HttpResponse(fuser)

    # return render(request, 'member/login.html')

def logout(request):
    del request.session['user_id'] # 개별 삭제
    del request.session['user_name'] # 개별 삭제
    request.session.flush() # 전체 삭제

    return redirect('/member/login')


def index(request):
    return render(request, 'miniproject/index.html')
