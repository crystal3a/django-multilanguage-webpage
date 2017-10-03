from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control',
                                                                       'placeholder': 'username'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'password'}))

