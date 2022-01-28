from distutils.command.upload import upload
from ssl import AlertDescription
from django.shortcuts import render,redirect

from miniproject.views import logout
from .models import Member
from django.http import HttpResponse
from .forms import UploadFileForm

def signup(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
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
        user_id = request.POST.get('id')
        password = request.POST.get('password')

        try:
            m = Member.objects.get(user_id=user_id, password=password)
        except Member.DoesNotExist as e:
            return render(request, 'member/loginfail.html')
        else:
            request.session['id'] = m.id
            request.session['user_name'] = m.user_name
        
        return redirect('/miniproject/maps')
    else:
        return render(request, 'member/login.html')

from .models import UploadFile
def img_show(request):
    id = request.GET.get('id')
    uploadFile = UploadFile.objects.get(id=id)
    return render(
        request, 'file/manage.html',
        {'uploadFile': uploadFile})

def loginfail(request):
    return render(request, 'member/loginfail.html')

def signupcheck(request):
    return render(request, 'member/signupcheck.html')

from django.views.decorators.http import require_POST


def delete(request):
    user = request.user
    user.delete()
    logout(request)
    context = {}
    return render(request, 'member/signupcheckup.html', context)