from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Maxes


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


class TestMaxesForm(forms.ModelForm):

    class Meta:

        model = Maxes
        fields = '__all__'
        exclude = ['user', ]

    def __init__(self, *args, **kwargs):
        super(TestMaxesForm, self).__init__(*args, **kwargs)
        self.fields['deadlift'].widget.attrs['min'] = 0
        self.fields['oh_press'].widget.attrs['min'] = 0
        self.fields['barbell_row'].widget.attrs['min'] = 0
        self.fields['bench_press'].widget.attrs['min'] = 0
        self.fields['squat'].widget.attrs['min'] = 0
        self.fields['pull_ups'].widget.attrs['min'] = 0
        self.fields['deadlift'].label = 'Martwy ciąg'
        self.fields['oh_press'].label = 'Wyciskanie nad głową'
        self.fields['barbell_row'].label = 'Wiosłowanie w opadzie'
        self.fields['bench_press'].label = 'Wyciskanie na ławce płaskiej'
        self.fields['squat'].label = 'Przysiad'
        self.fields['pull_ups'].label = 'Podciągnięcia na drążku'
