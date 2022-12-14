from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length = 150)
    phonenumber = forms.CharField(max_length=12)
    message = forms.CharField(widget= forms.Textarea, max_length= 2000)