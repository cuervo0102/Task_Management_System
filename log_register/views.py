import logging
import datetime
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
logs_user_register = logging.FileHandler('logs/users_register.log')
logs_user_register.setFormatter(formatter)
logger.addHandler(logs_user_register)

def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                logger.info(f"The account for user '{user.username}-{user.email}' has been successfully created")
                return redirect('/')
            except Exception as e:
                logger.error(f'Error saving user: {e}')
        else:
            logger.debug(f"Form data: {request.POST}")
            logger.debug(f"Is form valid? {form.is_valid()}")
    else:
        form = NewUserForm()

    return render(request, 'user_templates/register.html', context={'form':form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                logger.info(f'User {user.username}-{user.email} has logged in successfully')
                return redirect('/') 
            else:
                logger.error(f'Error logging in - Invalid credentials')
        else:
            logger.error(f'Error logging in - Form is not valid')
    else:
        form = AuthenticationForm()
    
    return render(request, 'user_templates/login.html', context={'login_form': form})
         

