from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'miniproject'

urlpatterns = [
    path('maps/', views.maps, name='maps'),
    path('session/', views.login_session, name='session'),
    path('logout/', views.logout, name='logout'),
    path('index/', views.index, name='index'),
    path('test/', views.test, name='test'),
]
