from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('reg/', views.register, name='reg'),
    path('home/', views.home, name='home'),
    path('home', views.home, name="home"),
    path('add_note/', views.add_note, name='add_note'),
    path('add_note', views.add_note, name='add_note'),
    path('notes/', views.notes, name='notes'),
    path('notes', views.notes, name='notes'),
    path('login/', auth_views.LoginView.as_view(template_name="notes/login.html")),
    path('logout/', views.logout_view, name="logout"),
]
