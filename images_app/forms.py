from django import forms
from .models import Post
from PIL import Image


class UserForm(forms.Form):
    name = forms.CharField()
    image = forms.CharField()
    cover = forms.ImageField()


