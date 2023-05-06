from django import forms
from django.core import validators

'''def check_letter(value):
    if value[0].lower()=='a':
        raise forms.ValidationError("invalid data")'''

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField(validators=[validators.MaxValueValidator(50)])
    Email=forms.EmailField()
    Re_enter_Email=forms.EmailField()
    Botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput(),required=False)
    mobileNumber=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator("[6-9]\d{9}")])
    
    
    def clean(self):
        e=self.cleaned_data['Email']
        r=self.cleaned_data["Re_enter_Email"]
        
        if e!=r:
            return forms.ValidationError("mail is not correct")
    def checking(self):
        b=self.cleaned_data["Botcatcher"]
        if len(b)>0:
            return forms.ValidationError("data is not validated")
        
        
    