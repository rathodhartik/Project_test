from django import forms
from api_crud.models import Student



class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            
        }
