from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'miniproject'

urlpatterns = [
    path('maps/', views.maps, name = 'maps'),
<<<<<<< HEAD
    path('login/',
        auth_views.LoginView.as_view(
            template_name='miniproject/login.html'
        ),
        name='login'
    ),
=======
    path('test/', views.test, name = 'test'),
>>>>>>> 5a6d900ecedbe0c7c4da4ce76e5430769e69a00f
]