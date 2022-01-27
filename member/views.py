from ssl import AlertDescription
from django.shortcuts import render,redirect
from .models import Member
from django.http import HttpResponse

def signup(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        user_name = request.POST.get('user_name')
        m = Member(
            user_id=user_id, password=password, user_name=user_name)
        m.save()
        return redirect('/member/login')
    else:
        return render(request, 'member/signup.html')

def login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

        try:
            m = Member.objects.get(user_id=user_id, password=password)
        except Member.DoesNotExist as e:
            return HttpResponse('로그인 실패')
        else:
            request.session['user_id'] = m.user_id
            request.session['user_name'] = m.user_name
        
        return render(request, 'miniproject/maps.html')
    else:
        return render(request, 'member/login.html')


def logout_custom(request):
    del request.session['user_id'] # 개별 삭제
    del request.session['user_name'] # 개별 삭제
    request.session.flush() # 전체 삭제
    return render(request, 'member/login.html')

def signupcheck(request):
    return render(request, 'member/signupcheck.html')