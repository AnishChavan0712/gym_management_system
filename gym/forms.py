from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['user', 'phone_number', 'address', 'plan', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
