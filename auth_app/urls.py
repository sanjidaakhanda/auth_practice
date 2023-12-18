
from django.urls import path
from . import views

urlpatterns = [
path('',views.home,name='home'),
path("register/",views.register,name = 'register'),
path('login/', views.user_login, name='login'),
path('out/', views.user_logout,name= 'out'),
path('profile/', views.profile,name= 'profile'),
#  path('logout/', views.user_logout, name='logout'),
 ]