from django.urls import path
from runner import views

urlpatterns = [
    path('', views.signup, name="signup"),
    path('home/', views.home, name="home"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('change_pass', views.change_pass, name="change_password")

]
