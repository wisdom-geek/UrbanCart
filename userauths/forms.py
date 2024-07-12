from django import forms 
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"John Doe"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"example@gmail.com"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"password123"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"password123"}))
        
    class Meta:
        model = User
        fields = ['username', 'email']