from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields +('age',)
        fields = ['username','email','first_name','last_name','age',]
        
class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields 
        fields = ['username','email','age',]