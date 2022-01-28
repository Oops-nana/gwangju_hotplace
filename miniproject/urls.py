from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'miniproject'

urlpatterns = [
    path('maps/', views.maps, name='maps'),
    path('login/',
         auth_views.LoginView.as_view(
             template_name='miniproject/login.html'
         ),
         name='login'
         ),

    path('logout/',
         auth_views.LogoutView.as_view(),
         name='logout'
         ),
    path('index/', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('comment/', views.postCommentAndStar, name='comment'),
    path('session/', views.login_session, name='session'),
    path('comment/', views.comment_create, name='comment_create'),
]
