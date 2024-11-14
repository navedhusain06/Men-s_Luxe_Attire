from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def ShopFun(request):
    shop_obj = Products.objects.all()
    return render(request, 'shop.html', {'shop_obj':shop_obj})

# @login_required
def homeFun(request):

    # messages.success(request, 'You have Successfully Logged in')
    return render(request, 'home.html')

def loginFun(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.warning(request, 'User is not found')
            return redirect('login')
        
        profile_obj = Profile.objects.filter(user = user_obj).first()
        
        if not profile_obj.is_verified:
            messages.error(request, 'Profile is not Varified Check your mail')
            return redirect('login')
        
        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request, 'Wrong Password')
            return redirect('login')
                
        login(request, user)
        return redirect('/')
    return render(request, 'login.html')

def registerFun(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password != password2:
            messages.warning(request, 'Password do not match')
            return redirect('register')
        
        if len(password) < 8:
            messages.warning(request, 'Password must be atleast 8 charcters long')
            return redirect('register')
        
        
        try:
        
            if User.objects.filter(username=username).first():
                messages.error(request, 'Username Is Taken')
                return redirect('register')
            
            if User.objects.filter(email=email).first():
                messages.error(request, 'Email is Taken')
                return redirect('register')
            
            user_obj = User.objects.create(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user=user_obj, auth_token=auth_token)
            profile_obj.save()
            send_mail_after_registration(email, auth_token)
            
            return redirect('token_send')
            
        except Exception as e:
            print(e)
            
    return render(request, 'register.html')

def token_send(request):
    return render(request, 'token_send.html')

def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your Account is already varified')
                return redirect('login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your Account Has been varified')
            return redirect('login')
        else:
            return HttpResponse('Your Token is Invalid')
            

    except Exception as e:
        print(e)

def send_mail_after_registration(email, token):
    subject = 'Your Accounts Need to be Varified'
    messages = f'Hi paste the link to varify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, messages, email_from, recipient_list)
    
     
from django.contrib.auth.tokens import default_token_generator

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user_obj = User.objects.filter(email=email).first()
        
        if user_obj:
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.get(user=user_obj)
            profile_obj.auth_token = auth_token
            profile_obj.save()
            send_password_reset_email(email, auth_token)
            messages.success(request, 'Password reset link has been sent to your email.')
            return redirect('forgot_password')
        else:
            messages.error(request, 'No account found with this email address.')
            return redirect('forgot_password')
    
    return render(request, 'forgot_password.html')


def reset_password(request, auth_token):
    profile_obj = Profile.objects.filter(auth_token=auth_token).first()
    
    if not profile_obj:
        messages.error(request, 'Invalid or expired password reset link.')
        return redirect('login')
    
    if request.method == 'POST':
        new_password = request.POST.get('password')
        user = profile_obj.user
        user.set_password(new_password)
        user.save()
        profile_obj.auth_token = ""
        profile_obj.save()
        messages.success(request, 'Your password has been reset successfully.')
        return redirect('login')
    
    return render(request, 'reset_password.html')

def send_password_reset_email(email, token):
    subject = 'Reset Your Password'
    message = f'Click the link below to reset your password:\nhttp://127.0.0.1:8000/reset-password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

    
def add_to_cart(request, product_id):
    # Fetch the product by ID
    product = get_object_or_404(Products, id=product_id)
    
    # Initialize the cart in session if it doesn't exist
    cart = request.session.get('cart', {})
    
    # Check if the product is already in the cart
    if product_id in cart:
        cart[product_id]['quantity'] += 1
    else:
        cart[product_id] = {
            'name': product.name,
            'price': product.price,
            'quantity': 1
        }
    
    # Save the cart back to the session
    request.session['cart'] = cart
    messages.success(request, f"{product.name} added to cart!")
    
    return redirect('shop') 


# views.py
from django.shortcuts import render

def view_cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'cart.html', {'cart': cart, 'total_price': total_price})


def logoutFun(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'logout.html')

def profile(request):
    user_obj = request.user  
    return render(request, 'profile.html', {'user_obj':user_obj})

def product_detail(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    size_obj = Size.objects.all()
    return render(request, 'product-detail.html', {'product': product})