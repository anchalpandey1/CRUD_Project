from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    
    class Meta:
        # model=Userfields=['name','email','password']
        model=User
        fields = "__all__"  
        # widgets={
        #      'name':forms.TextInput(attrs={'class':'form-control'}),
        #      'email':forms.EmailInput(attrs={'class':'form-control'}),
        # #     'password':forms.PasswordInput(render_values=True, attrs={'class':'form-control'}),
        # }