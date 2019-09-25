from django import forms
from django.contrib.auth.models import User


from django.contrib.auth.forms import  AuthenticationForm
from .models import Profile

class RegisterForm(forms.Form):
    username         = forms.CharField()
    email            = forms.EmailField()
    password         = forms.CharField(widget=forms.PasswordInput)
    confirmpassword  = forms.CharField(
        label='confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
    	    raise forms.ValidationError("user name is already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
    	    raise forms.ValidationError("Email is taken")
        return email


    def clean(self):
        data                 = self.cleaned_data
        password             = self.cleaned_data.get('password')
        confirmpassword      = self.cleaned_data.get('confirmpassword')
        if confirmpassword  != password:
            raise forms.ValidationError("passwords must match.")
        return data


class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']