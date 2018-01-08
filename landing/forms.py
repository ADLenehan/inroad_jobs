from django import forms
from landing.models import SignUp, Purpose


class SignUpForm(forms.ModelForm):
    purposes = Purpose.objects.all()
    name = forms.CharField(max_length=200, help_text="Elon", required=True)
    email = forms.EmailField(max_length=200, help_text="elon@gmail.com", required=True)
    purpose = forms.ModelChoiceField(queryset=purposes, widget=forms.RadioSelect(), required=True, empty_label=None)

    class Meta:
        model = SignUp
        fields = ['name','email','purpose']