from django import forms

class CheckUpdateForm(forms.Form):
    code = forms.CharField(label='Enter Code', max_length=10)
    number = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'No number'}))
