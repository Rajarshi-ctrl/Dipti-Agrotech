from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('product/', views.product, name='product'),
    path('detail/', views.detail, name='detail'),
    path('login/', views.userlogin, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.userlogout, name="logout"),

]
