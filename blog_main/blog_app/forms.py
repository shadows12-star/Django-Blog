from .models import comments
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
class CommentForm(forms.ModelForm):
        
        class Meta:
            model = comments
            fields = ("comment",)
    