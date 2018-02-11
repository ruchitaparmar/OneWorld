from django import forms
from .models import Refugee, Shelter


class RefugeeForm(forms.ModelForm):

    class Meta:
        model = Refugee
        exclude = ('Comments', 'bID')


class ShelterForm(forms.ModelForm):

    class Meta:
        model = Shelter
        exclude = ('bID', )


'''
class addRefugee(forms.ModelForm):

	class Meta:
		model = Refugee
		exclude = ['dob', 'refImage', 'comments']
'''
