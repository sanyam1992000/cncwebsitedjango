from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import UserProfile


course = (
    ('BTECH', 'Btech'),
    ('MTECH', 'Mtech'),
    ('BCA', 'BCA'),
    ('MCA', 'MCA'),
    ('BSC', 'Bsc'),
    ('MSC', 'Msc'),
    ('MBA', 'MBA'),
)

branch = (
    ('CE', 'CE'),
    ('IT', 'IT'),
    ('ECE', 'ECE'),
    ('ECS', 'ECS'),
    ('EIC', 'EIC'),
    ('EL', 'EL'),
    ('MECH', 'MECH'),
    ('CIVIL', 'CIVIL'),
)


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    email = forms.EmailField(label='Email ID')

    password1 = forms.CharField(label='Password', min_length=6,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', min_length=6,)
    roll_no = forms.IntegerField(label='Roll No.', min_value=10000000000, max_value=100000000000)
    course = forms.ChoiceField(label='Course', choices=course)
    branch = forms.ChoiceField(label='Branch', choices=branch)
    phoneno = forms.IntegerField(label='Phone No.', min_value=6000000000, max_value=9999999999)
    icard = forms.ImageField(label='I-card Front', allow_empty_file=True, required=False)

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')
        if p1 and p2:
            if p1 != p2:
                raise ValidationError('Password Mismatch')

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError('Email is already registered.')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = User.objects.filter(username=username)
        spaces = username.count(' ')
        if qs.exists():
            raise ValidationError('Username is already registered.')
        elif spaces > 0:
            raise ValidationError('Spaces not allowed in Username')
        return username

    def clean_roll_no(self):
        roll_no = self.cleaned_data['roll_no']
        qs = UserProfile.objects.filter(roll_no=roll_no)
        if qs.exists():
            raise ValidationError('Roll Number is already registered.')
        return roll_no


class UserLogin(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', min_length=6,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class EditUser(forms.ModelForm):
    username = forms.CharField(label='Username',max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', min_length=6,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'password1']

    # def clean_password1(self):
    #     password = self.cleaned_data['password1']
    #     if not self.user.check_password(password):
    #         raise ValidationError('Invalid password')
    #     return password

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     qs = User.objects.filter(username=username)
    #     spaces = username.count(' ')
    #     if u
    #     elif qs.exists():
    #         raise ValidationError('Username is already registered.')
    #     elif spaces > 0:
    #         raise ValidationError('Spaces not allowed in Username')
    #     return username

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     qs = User.objects.filter(email=email)
    #     if qs.exists():
    #         raise ValidationError('Email is already registered.')
    #     return email


class EditStudentProfile(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['pic', 'phoneno']


class ChangePassword(forms.ModelForm):
    current_password = forms.CharField(label='Current Password',min_length=6,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password = forms.CharField(label='New Password',min_length=6,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_new_password = forms.CharField(label='Confirm New Password',min_length=6,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['current_password', 'new_password', 'confirm_new_password']