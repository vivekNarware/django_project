from django import forms
from Gym.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields={'name','age','gender','locality','email','number'}

