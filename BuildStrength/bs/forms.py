from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    username = forms.CharField(max_length=150, label="nazwa użytkownika")
    password = forms.CharField(max_length=150, label="hasło", widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):

    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        help_texts = {"username": ""}
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['password1'].label = 'Hasło'
        self.fields['password2'].label = 'Powtórz hasło'
        self.fields['username'].label = 'Login'
