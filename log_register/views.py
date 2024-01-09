import logging
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required


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
                return redirect('/edit-profile/')
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
                UserProfile.objects.create(user=user)
                login(request, user)
                
                logger.info(f'User {user.username}-{user.email} has logged in successfully')
                return redirect('/tasks/create-task') 
            else:
                logger.error(f'Error logging in - Invalid credentials')
        else:
            logger.error(f'Error logging in - Form is not valid')
    else:
        form = AuthenticationForm()
    
    return render(request, 'user_templates/login.html', context={'login_form': form})



def logout_request(request):
	logout(request)
	return redirect('/login')

@login_required
def edit_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('edit_user_profile')
    else:
        form = UserProfileForm()

    return render(request, 'user_templates/edit_user_profile.html', {'form': form})


def test(request):
    return render(request, 'user_templates/test.html')
         

