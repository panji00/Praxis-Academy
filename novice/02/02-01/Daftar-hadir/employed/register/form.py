from django import forms
from .models import register


class EmployedForm(forms.ModelForm):
    class Meta:
        model = register
        fields = '__all__'
        labels = {
            'fullname': 'Full Name',
            'emp_code': 'EMP. Code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployedForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False