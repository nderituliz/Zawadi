from django import forms
from django.forms import ModelForm
from .models import Profile, Projects, Categories


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_photo", "bio", "contact"]
