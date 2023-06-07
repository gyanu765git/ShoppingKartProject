
from django.urls import path
from shopping_app import views


urlpatterns = [
    path('', views.Index.as_view(), name='homepage'),
    path('store/', views.store , name='store'),
    path('cart/', views.Cart.as_view() , name='cart'),
    path('signup/',views.SignUp_Request, name='signup'),
    path('login/', views.Login_Request, name='login'),
    path('logout/', views.Logout_Request , name='logout'),
    path('next/',views.NextStep, name='next')
]
