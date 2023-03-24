from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpRequest
from myfirstapp.models import Item

# Create your views here.
def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items,})

def fashion(request):
    return render(request, 'fashion.html')

def electronic(request):
    return render(request, 'electronic.html')

def jewellery(request):
    return render(request, 'jewellery.html')

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email in use')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username in use')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
    else:
        return render(request, 'register.html') #, {'username': username,}