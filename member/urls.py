from . import views
from django.urls import path

app_name = 'member'


urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]