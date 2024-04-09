from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

UserModel = get_user_model()


class ProjectUserCreation(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class ProjectUserLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))


class ProjectUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel
