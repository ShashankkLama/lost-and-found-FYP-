
from django.urls import path
from app1 import views



urlpatterns = [
    path('signup', views.SignupPage, name='signup'),
        
    path('', views.LoginPage, name='login'), 
    
    path('home/', views.HomePage, name='home'), 

    path('logout/', views.LogoutPage, name ='logout'), 
]