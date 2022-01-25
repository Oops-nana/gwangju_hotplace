from django.urls import path
from . import views

app_name = 'miniproject'

urlpatterns = [
    path('maps/', views.maps, name = 'maps'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('signup/', views.signup, name = 'signup'),
]