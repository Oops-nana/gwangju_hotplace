from . import views
from django.urls import path

app_name = 'member'


urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('signupcheck/', views.signupcheck, name='signupcheck'),
    path('loginfail/', views.loginfail, name='loginfail'),
    path('manage/', views.delete, name='manage'),
]