from django import forms
from  .models import Profile , Projects
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = []
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = []
       