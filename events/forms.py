from django import forms
from django.core.exceptions import ValidationError


class SuggestEvent(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    email = forms.EmailField(label='Email ID')

    password1 = forms.CharField(label='Password', min_length=6,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', min_length=6,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    roll_no = forms.IntegerField(label='Roll No.', min_value=10000000000, max_value=100000000000)
    course = forms.ChoiceField(label='Course', choices=course)
    branch = forms.ChoiceField(label='Branch', choices=branch)
    phoneno = forms.IntegerField(label='Phone No.', min_value=6000000000, max_value=9999999999)