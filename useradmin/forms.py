from django import forms

class AccountForm(forms.Form):
    user_name = forms.CharField(label='Your username', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)