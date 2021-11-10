from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .services import get_years_range



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email',)


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match')
        return cd['password2']



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#________________________________________________

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email',)


class ProfileEditForm(forms.ModelForm):
    date_of_birth =  forms.DateField(widget=forms.SelectDateWidget(years=get_years_range()))
    photo =forms.ImageField(widget=forms.FileInput(attrs={'class':'chooseFileButton','row':1,}))
    class Meta:
        model = Profile
        fields = ('date_of_birth','photo')


