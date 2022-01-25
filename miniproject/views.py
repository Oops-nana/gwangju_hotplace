from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse

def maps(request):
    return render(request, 'miniproject/maps.html')

def login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        try:
            m = miniproject.objects.get(user_id=user_id, user_pw=user_pw)
        except miniproject.DoesNotExist as e:
            return HttpResponse('아이디와 비밀번호를 확인해주세요.')
        else:
            request.session['user_id'] = m.user_id
            request.session['user_name'] = m.user_name

        # 회원정보 조회 실패 시 예외 발생
        return redirect('miniproject:login')
    else:
        return render(request, 'member/login_custom.html')

def index(request):
    return render(request, 'miniproject/index.html')