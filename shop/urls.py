from django.urls import path

from shop import views

urlpatterns = [
    path('', views.home),
    path('<slug:c_slug>/', views.home, name='cate'),
    path('<slug:c_slug>/<slug:p_slug>', views.prod, name='pro'),
    path('search', views.searching, name='search')


]
