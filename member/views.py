from distutils.command.upload import upload
from ssl import AlertDescription
from django.shortcuts import render,redirect
from .models import Member
from django.http import HttpResponse
from .forms import UploadFileForm

def signup(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        user_name = request.POST.get('user_name')
        
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploadFile = form.save()
            name = uploadFile.file.name
        else:
            form = UploadFileForm()
            name = ''
            
        m = Member(
            user_id=user_id, password=password, user_name=user_name, file_name = name)
        m.save()
        return redirect('/member/signupcheck')
    else:
        return render(request, 'member/signup.html')

def login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

        try:
            m = Member.objects.get(user_id=user_id, password=password)
        except Member.DoesNotExist as e:
            return render(request, 'member/loginfail.html')
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

def loginfail(request):
    return render(request, 'member/loginfail.html')

def signupcheck(request):
    return render(request, 'member/signupcheck.html')