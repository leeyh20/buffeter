from django import forms
from .models import UserProfile

class AccountForm(forms.Form):
    user_name = forms.CharField(label='Your username', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
  class Meta:
    model = UserProfile
    fields = ('birth_date', 'gender', 'profile_pic')