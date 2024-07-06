from django import forms
from .models import Comments,Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','image','description']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']