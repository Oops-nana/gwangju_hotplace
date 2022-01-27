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
<<<<<<< HEAD


=======
    path('test/', views.test, name='test'),
>>>>>>> 11423cffaf13ad01bc3a5e064a9e340e5f34c8b1
]
