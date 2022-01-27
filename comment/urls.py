from . import views
from django.urls import path

app_name = 'comment'


urlpatterns = [
    path('review/', views.review, name='review'),
]