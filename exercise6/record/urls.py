from django.urls import path

from . import views

urlpatterns = [
    path('', views.mylogin, name='login'),
    path('logout/', views.mylogout, name='logout'),
    path('request/', views.home, name='home'),
    path('history/', views.history, name='history'),
]
