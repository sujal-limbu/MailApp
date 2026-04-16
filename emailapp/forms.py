from django import forms

class EmailForm(forms.Form):
    recipient = forms.EmailField(label='To')
    message = forms.CharField(label='Message')
    subject = forms.CharField(label='Subject')

    
    