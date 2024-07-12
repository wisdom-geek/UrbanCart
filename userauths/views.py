from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)     
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, your account was created successfully. Please log in.")
            return redirect('userauths:login')
    else:
        form = UserRegisterForm()
           
    context = {
        'form': form,
    }
    return render(request, 'userauth/sign-up.html', context)

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in.")
        return redirect("core:index")
    
    if request.method == 'POST':        
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Login successful.")
                return redirect('core:index')  
            else:
                messages.warning(request, "Invalid email or password.")
        else:
            messages.warning(request, "Invalid email or password.")
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'userauth/login.html', context)

def logout_view(request):
    logout(request)
    
    return redirect('userauths:login')