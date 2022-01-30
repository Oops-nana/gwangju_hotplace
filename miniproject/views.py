from . import CommentForms
from main.models import Comment
from django.utils import timezone
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from main.models import Comment, CommonPlace, museumDetail
from django.forms.models import model_to_dict
from member.models import Member


def maps(request):
    if request.session.get('id'):
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
    else:
        return redirect(reverse('member:login'))


# def login_session(request):
#     user_pk = request.session.get('id')

#     if user_pk:
#         fuser = Member.objects.get(pk=user_pk)
#     return HttpResponse(fuser)

    # return render(request, 'member/login.html')


def logout(request):
    del request.session['id']  # 개별 삭제
    del request.session['user_name']  # 개별 삭제
    request.session.flush()  # 전체 삭제

    return redirect('/member/login')


def login_session(request):
    user_pk = request.session.get('id')
    print(user_pk)

    if user_pk:
        fuser = Member.objects.get(pk=user_pk)
        print(fuser)
        return HttpResponse(user_pk)


@csrf_exempt
def postCommentAndStar(request):
    if request.method == 'POST':

        comment = request.POST.get('inputValue')
        print(comment)
        star = request.POST.get('starValue')
        star = int(star)
        print(star)
        place_name = request.POST.get('place_name')
        print(place_name)
        place = CommonPlace.objects.get(place_name=place_name)
        # user_id = request.POST.get('user_id')
        # 로그인 후 세션에서 바로 뽑아서 넣어줌.
        user_id = request.session.get('id')
        print(user_id)
        user = Member.objects.get(pk=user_id)
        print(comment, star, place, user)
        Comment.objects.create(
            content=comment,
            rate=star,
            place_id=place,
            id=user,
            # date=timezone.now()
        )
        return redirect('/miniproject/maps')

    return JsonResponse(request, {'msg': '정상범위가 아닙니다.'})


# def comment_create(request):
#     form = CommentForms()
#     return render(request, 'miniproject/comment.html', {'form': form})


def comment_create(request):
    if request.method == 'POST':
        form = CommentForms(request.POST)
        comment = form.save(commit=False)
        content = form.cleaned_data['content']

        date = timezone.now()
        star = form.cleaned_data['star'].value
        user_id = request.session.get('id')
        user = Member.objects.get(pk=user_id)
        print("--------------------")
        print(content, date, star, user_id)
        print("--------------------")
        Comment.objects.create(
            id=user,
            rate=star,
            date=date,
            content=content
        )
        comment.save()
        # 댓글 목록 불러오기 url실행
        return redirect('')
    else:
        form = CommentForms()
    context = {'form': form}
    return render(request, 'miniproject/comment.html', context)
