from django.shortcuts import render, redirect
from .forms import RefugeeForm, ShelterForm
from .models import Refugee, Shelter
from .filters import RefugeeFilter
from django.core.files.storage import FileSystemStorage
# Create your views here.


def search(request):
	refugee_list = Refugee.objects.all()
	refugee_filtered = RefugeeFilter(request.GET, queryset=refugee_list)
	return render(request, 'search.html', {'refugee_filtered': refugee_filtered})


def dashboard(request):
    return render(request, 'dashboard.html')


def addRefugee(request):
    form = RefugeeForm()
    return render(request, 'RefugeeForm.html', {'form': form})


def addShelter(request):
    form = ShelterForm()
    return render(request, 'ShelterForm.html', {'form': form})


def refugeeCard(request, pk):
	refugee = Refugee.objects.get(pk=pk)
	return render(request, 'RefugeeCard.html', {'refugee': refugee})


def shelterCard(request, pk):
	shelter = Shelter.objects.get(pk=pk)
	return render(request, 'ShelterCard.html', {'shelter': shelter})


def showRefugee(request):
	if request.method == "POST":
		form = RefugeeForm(request.POST, request.FILES)
		if form.is_valid():
			refugee = form.save(commit=False)
			refImage = request.FILES["refImage"]
			fs = FileSystemStorage()
			fs.save('media/' + str(refugee.pk) + refImage.name[-4:], refImage)

			refugee.bID = request.user.username
			refugee.save()
			return redirect('/bo/refugeeCard/' + str(refugee.pk))
	else:
		form = RefugeeForm()
	return render(request, 'RefugeeForm.html', {'form': form})


def showShelter(request):
	if request.method == "POST":
		print("Post hai shelter")
		form = ShelterForm(request.POST)
		if form.is_valid():
			shelter = form.save(commit=False)
			shelter.bID = request.user.username
			shelter.save()
			return redirect('/bo/shelterCard/' + str(shelter.pk))
	else:
		form = ShelterForm()
	return render(request, 'ShelterForm.html', {'form': form})
