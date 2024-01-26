from django.urls import path
from accounts import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('logout', views.logout, name='logout')

]
