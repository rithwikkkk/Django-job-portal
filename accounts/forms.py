from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    ROLE_CHOICES = (
        ('seeker', 'Job Seeker'),
        ('recruiter', 'Recruiter'),
    )

    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'role')
