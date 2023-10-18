from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


from account.models import *


# get custom user
User = get_user_model()





class LoginForm(forms.Form):
    email= forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={
        "type":"email",
        "class":"form-control",
        "placeholder":"Email",
        "name":"u_name",
        }
    ))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={
        "type":"password",
        "class":"form-control",
        "placeholder":"Password",
        "name":"password",
        }
    ))

    def clean(self):
        email=self.cleaned_data.get("email")
        password=self.cleaned_data.get("password")
        if email and password:
            user=authenticate(email=email,password=password)
            if not user:
                raise forms.ValidationError("Email or Password is incorrect !")




        return super(LoginForm, self).clean()



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""


######################################################################################################

class RegisterForm(UserCreationForm):
    name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={
        "type":"text",
        "name":"name",
        "class":"form-control",
        "placeholder":"Name",
    }))

    surname = forms.CharField(max_length=200,widget=forms.TextInput(attrs={
       
        "type":"text",
        "name":"name",
        "class":"form-control",
        "placeholder":"Surname",
    }))

    


    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={
        "type":"email",
        "name":"email",
        "class":"form-control",
        "placeholder":"example@gmail.com",

        }
    ))

    password1=forms.CharField(max_length=100,widget=forms.PasswordInput(
        attrs={
        "type":"password",
        "name":"password",
        "class":"form-control",
        "placeholder":"password 1",

        }
    ))
    password2=forms.CharField(max_length=100,widget=forms.PasswordInput(
        attrs={
        "type":"password",
        "name":"c_password",
        "class":"form-control",
        "placeholder":"password again",
        }
    ))


    class Meta:
        model = User
        fields = ("name","surname","email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")

        try:
            match = MyUser.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError("This email already exists. Please try another one!")



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""




class EncyrptionForm(forms.Form):
    text = forms.CharField(max_length=200,widget=forms.TextInput(attrs={
        "type":"text",
        "name":"first_name",
        "class":"form-control",
        "placeholder":"Your Text",
    }))

    key = forms.CharField(max_length=200,widget=forms.TextInput(attrs={
       
        "type":"text",
        "name":"phone",
        "class":"form-control",
        "placeholder":"Your Key Text Format",
    }))

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""


class DecyrptionForm(forms.Form):
    text = forms.CharField(max_length=200,widget=forms.TextInput(attrs={
        "type":"text",
        "name":"first_name",
        "class":"form-control",
        "placeholder":"Encrypted Text",
    }))

    key = forms.CharField(max_length=200,widget=forms.TextInput(attrs={
       
        "type":"text",
        "name":"phone",
        "class":"form-control",
        "placeholder":"Your Key Binary Format*",
    }))

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""