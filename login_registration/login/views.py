from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    errors = User.objects.validate(request.POST)
    if errors:
        for field, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    User.objects.register(request.POST)

    return redirect('/success')

def login(request):
    result = User.objects.authenticate(request.POST['email'], request.POST['password'])
    if result == False:
        messages.error(request, 'Invalid Email or Password')
        #return redirect('/')
    return redirect('/')

def success(request):
    context = {
        'user': User.objects.all()
    }
    return render(request, 'success.html', context)