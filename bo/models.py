from django.db import models
from django.core.validators import RegexValidator


class Offspring(models.Model):
	fullNameOfOffspring = models.CharField(max_length=100)


class Refugee(models.Model):
	alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric')
	ID = models.CharField(
		max_length=16, validators=[alphanumeric], primary_key=True
	)

	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)

	dob = models.DateField()

	nationality = models.CharField(max_length=50)

	bID = models.ForeignKey('signIn.Benefactor', on_delete=models.CASCADE)

	refImage = models.FileField(upload_to="Images/")

	maritalStatusChoices = (
		('M', 'Married'),
		('S', 'Single')
	)
	maritalStatus = models.CharField(choices=maritalStatusChoices, default='S')

	fullNameOfSpouse = models.CharField(max_length=100)
	numOfOffspring = models.IntegerField()
	fullNameOfOffspring = models.ForeignKey('Offspring', on_delete=models.CASCADE)
	fullNameOfFather = models.CharField(max_length=100)
	fullNameOfMother = models.CharField(max_length=100)
	Comments = models.CharField(max_length=500)
