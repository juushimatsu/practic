from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'country', 'city', 'street', 'house', 'apartment_number']

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'username',
                'placeholder': 'Введите логин',
            }
        ),
        required=True,
        validators=[RegexValidator(r'^[a-zA-Z0-9]*$', "Введен неверный логин")],
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'autocomplete': 'email',
                'placeholder': 'Введите электронную почту',
            }
        ),
        required=True
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Введите пароль',
            }
        ),
        required=True
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Повторите пароль',
            }
        ),
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def save(self, commit=True):
        user = super().save(commit)
        Profile.objects.create(user=user)  # Создаем профиль для нового пользователя
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'username',
                'placeholder': 'Логин',
            }
        ),
        required=False
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'placeholder': 'Пароль',
            }
        ),
        required=False
    )

    error_messages = {
        "invalid_login": (
            "Введите логин и пароль правильно."
        ),
    }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('Введите пароль', code='invalid')
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('Введите логин', code='invalid')
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('Такого пользователя не существует', code='invalid')
        return username


