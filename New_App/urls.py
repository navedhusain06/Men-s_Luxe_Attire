from django.urls import path
from .views import *

urlpatterns = [
    path('shop', ShopFun, name='shop'),
    path('', homeFun, name='home'),
    path('login/', loginFun, name='login'),
    path('logout/', logoutFun, name='logout'),
    path('register/', registerFun, name='register'),
    path('token/', token_send, name='token_send'),
    path('verify/<auth_token>', verify, name='verify'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('reset-password/<auth_token>/', reset_password, name='reset_password'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('profile', profile, name='profile'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
]
