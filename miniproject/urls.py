from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'miniproject'

urlpatterns = [
    path('maps/', views.maps, name='maps'),
    path('logout/', views.logout, name='logout'),
    path('comment/', views.postCommentAndStar, name='comment'),
]
