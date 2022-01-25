from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'miniproject'

urlpatterns = [
    path('maps/', views.maps, name = 'maps'),
    path('login/',
        auth_views.LoginView.as_view(
            template_name='miniproject/login.html'
        ),
        name='login'
    ),
    path('test/', views.test, name = 'test'),
]