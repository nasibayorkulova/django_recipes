from django import forms
from .models import Recipes
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ('title', 'category', 'description', 'photo', 'is_published')
        widgets = {
            "title": forms.TextInput({
                "class": "form-control"
            }),
            "category": forms.Select({
                "class": "form-control"
            }),
            "description": forms.Textarea({
                "class": "form-control",
                "rows": 5
            }),

        }


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Логин", max_length=20, widget=forms.TextInput({
        "class": "form-control"
    }))
    firstname = forms.CharField(label="Имя", max_length=50, widget=forms.TextInput({
        "class": "form-control"
    }))
    lastname = forms.CharField(label="Фамилия", max_length=50, widget=forms.TextInput({
        "class": "form-control"
    }))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput({"class": "form-control"}))
    password2 = forms.CharField(label="Подтвердить пароль", widget=forms.PasswordInput({"class": "form-control"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput({"class": "form-control"}))

    class Meta:
        model = User
        fields = ("username", "firstname", "lastname", "password1", "password2", "email")


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Логин", max_length=20, widget=forms.TextInput({
        "class": "form-control"
    }))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput({"class": "form-control"}))