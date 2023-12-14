from django import forms
from django.core import validators

class TeachersRegistration(forms.Form):
    first_name= forms.CharField(label="Enter your First name")
    last_name= forms.CharField(initial='Blog')
    email= forms.EmailField(initial='xyz@gmail.com',disabled=True)
    password=forms.CharField(widget=forms.PasswordInput)
    repassword=forms.CharField(widget=forms.PasswordInput)
    textarea=forms.CharField(widget=forms.Textarea)
    file=forms.CharField(widget=forms.FileInput)
    checkBox=forms.CharField(widget=forms.CheckboxInput)

    def clean(self):
        clean_data=super().clean()
        rightpass=self.cleaned_data['password']
        wrongpass=self.cleaned_data['repassword']

        if rightpass != wrongpass:
            raise forms.ValidationError("Wrong Password")

        