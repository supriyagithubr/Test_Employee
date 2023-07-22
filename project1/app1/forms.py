from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'e_id': 'EMPLOYEE_ID',
            'e_name': 'EMPLOYEE NAME',
            'salary': 'SALARY',
            'city': 'CITY',
            'c_name' : 'COMPANY NAME'
        }

        widgets = {
            'e_id': forms.NumberInput(attrs={'class':'form-control', 'autocomplete':'off'}),
            'e_name': forms.TextInput(attrs={'class':'form-control', 'autocomplete':'off'}),
            'salary': forms.NumberInput(attrs={'class':'form-control', 'autocomplete':'off'}),
            'city':forms.TextInput(attrs={'class':'form-control', 'autocomplete':'off'}),
            'c_name': forms.TextInput(attrs={'class':'form-control', 'autocomplete':'off'})
        }

