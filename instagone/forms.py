from django import forms
from .models import Image,Profile


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }   
class ProfileUploadForm(forms.ModelForm):
	class Meta:
		model = Profile
		
		exclude = ['user']
class ProfileForm(forms.ModelForm):
	model = Profile
	username = forms.CharField(label='Username',max_length = 25)
	
	bio = forms.CharField(label='Image Caption',max_length=450)
	image = forms.ImageField(label = 'Image Field')