from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from login.models import userprofile
#from login.models import userprofile
class SignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=['username','password1','password2','email','first_name','last_name']
class ProfilePic(forms.ModelForm):
	class Meta:
		model=userprofile
		fields=['profile_pic']
		