from django import forms
from .models import Profile


class CreateSubEvent(forms.ModelForm):
    class Meta:
        model = Profile
        password1 = forms.CharField(max_length=16, widget=forms.PasswordInput)
        fields = ['username', 'first_name',
                  'last_name', 'user_email', 'pssword', 'password1']
