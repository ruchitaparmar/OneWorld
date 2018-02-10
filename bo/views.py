from django.shortcuts import render, redirect
from .forms import RefugeeForm, ShelterForm
from .models import Refugee, Shelter
from .filters import RefugeeFilter
from django.core.files.storage import FileSystemStorage
# Create your views here.


def search(request):
	refugee_list = Refugee.objects.all()
	refugee_filtered = RefugeeFilter(request.GET, queryset=refugee_list)
	return render(request, 'bo/search.html', {'refugee_filtered': refugee_filtered})


def dashboard(request):
    return render(request, 'bo/dashboard.html')


def addRefugee(request):
    form = RefugeeForm()
    return render(request, 'bo/RefugeeForm.html', {'form': form})


def addShelter(request):
    form = ShelterForm()
    return render(request, 'bo/ShelterForm.html', {'form': form})


def refugeeCard(request, pk):
	refugee = Refugee.objects.get(pk=pk)
	return render(request, 'bo/RefugeeCard.html', {'refugee': refugee})


def shelterCard(request, pk):
	shelter = Shelter.objects.get(pk=pk)
	return render(request, 'bo/ShelterCard.html', {'shelter': shelter})


def showRefugee(request):
	if request.method == "POST":
		form = RefugeeForm(request.POST, request.FILES)
		if form.is_valid():
			refugee = form.save(commit=False)
			refugee.save()
			refImage = request.FILES["refImage"]
			fs = FileSystemStorage()
			fs.save('media/' + str(refugee.pk) + '.jpg', refImage)
			return redirect('refugeeCard', pk=refugee.pk)
	else:
		form = RefugeeForm()
	return render(request, 'bo/RefugeeForm.html', {'form': form})


def showShelter(request):
	if request.method == "POST":
		print("Post hai shelter")
		form = ShelterForm(request.POST)
		if form.is_valid():
			shelter = form.save(commit=False)
			shelter.save()
			return redirect('shelterCard', pk=shelter.pk)
	else:
		form = ShelterForm()
	return render(request, 'bo/ShelterForm.html', {'form': form})
