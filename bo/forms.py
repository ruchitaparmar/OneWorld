from django import forms
from .models import Refugee, Shelter


class RefugeeForm(forms.ModelForm):

    class Meta:
        model = Refugee
        exclude = ('Comments',)


class ShelterForm(forms.ModelForm):

    class Meta:
        model = Shelter
        exclude = ()


'''
class addRefugee(forms.ModelForm):

	class Meta:
		model = Refugee
		exclude = ['dob', 'refImage', 'comments']
'''
