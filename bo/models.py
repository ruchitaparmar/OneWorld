from django.db import models
from django.core.validators import RegexValidator


class Shelter(models.Model):
	shelterID = models.CharField(max_length=8, primary_key=True)
	bID = models.ForeignKey('signIn.Benefactor', on_delete=models.CASCADE)
	latitude = models.CharField(max_length=50)
	longitude = models.CharField(max_length=50)
	status = models.CharField(max_length=50)
	health = models.CharField(max_length=50)
	food = models.CharField(max_length=50)
	numberOfRefugees = models.IntegerField()

	def __str__(self):
		return '%s %s' % (self.shelterID, self.bID)


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
	sID = models.ForeignKey('Shelter', on_delete=models.CASCADE)

	# refImage = models.FileField(upload_to="Images/")
	refImage = models.FileField()

	maritalStatusChoices = (
		('M', 'Married'),
		('S', 'Single')
	)
	maritalStatus = models.CharField(choices=maritalStatusChoices, default='S', max_length=1)

	fullNameOfSpouse = models.CharField(max_length=100)
	numOfOffspring = models.IntegerField()
	fullNameOfOffspring = models.CharField(max_length=100)
	fullNameOfFather = models.CharField(max_length=100)
	fullNameOfMother = models.CharField(max_length=100)
	Comments = models.CharField(max_length=500)

	def __str__(self):
		return '%s %s' % (self.ID, self.firstName)
