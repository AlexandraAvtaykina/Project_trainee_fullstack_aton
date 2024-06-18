from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from main.models import User, Client


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserLoginForm(StyleFormMixin, AuthenticationForm):

    class Meta:
        model = User
        fields = ('login', 'password1',)


class UserRegisterForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('fullname', 'login', 'password1', 'password2',)


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['status']


class ClientStatusForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = ('status',)
