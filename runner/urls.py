from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name="signup"),#redirect signup method 
    path('home/', views.home, name="home"), #redirect home method after authenticate user
    path('login/', views.login_page, name="login"),# redirect to login method for authentication
    path('logout/', views.logout_page, name="logout"),# redirect to logout method
    path('change_pass/', views.change_pass, name="change_password"),# redirect to the change_password method
     path('update/', views.update_profile, name="update")# redirect to the update_profile method
]
