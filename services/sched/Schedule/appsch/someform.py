from django import forms
from django.contrib.auth.models import User
from .models import Userinfo, LessonDate
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput, EmailInput


class LessonForm(forms.ModelForm):
    class Meta:
        model = LessonDate
        fields = ['instructor', 'owner', 'start_lesson', 'end_lesson', 'comment']


class UserinfoForm(forms.ModelForm):
    class Meta:
        model = Userinfo
        fields = ['First_name', 'Last_name', 'About_me', 'picture']



class LoginForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def save(self, commit=True):
        user = super(LoginForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user