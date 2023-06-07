
from django.urls import path
from shopping_app import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
    path('stock/', views.ProductStock , name='stock'),
    path('cart/', views.Cart.as_view() , name='cart'),
    path('signup/',views.SignUp_Request, name='signup'),
    path('login/', views.Login_Request, name='login'),
    path('logout/', views.Logout_Request , name='logout'),
    path('next/',views.NextStep, name='next')
]
