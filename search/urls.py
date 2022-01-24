from django.urls import path
from . import views
urlpatterns = [
    path('search/', SearchFormView.as_view(), name='search'),
]
