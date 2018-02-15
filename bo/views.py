from django.shortcuts import render, redirect
from .forms import RefugeeForm, ShelterForm
from .models import Refugee, Shelter
from .filters import RefugeeFilter
from django.core.files.storage import FileSystemStorage
import kairos_face
import os

# put your keys in kairos face
kairos_face.settings.app_id = "5af78aaa"
kairos_face.settings.app_key = "d049a1282b848d0846edab22a2982e0d"
gallery_name = 'development'
# Create your views here.


def heatmap(request):
	shelters = Shelter.objects.all()
	latlong = {}
	latlong['coors'] = []
	for shelter in shelters:
		lat = shelter.latitude
		longi = shelter.longitude
		latlong['coors'].append({'lat': lat, 'longi': longi})
	return render(request, 'heatmap.html', latlong)


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


def sendRequest(request):
	return render(request, 'sendRequest.html')


def refugeeCard(request, pk):
	refugee = Refugee.objects.get(pk=pk)
	imagePath = refugee.refImage.path
	imagePath = '/media/' + str(refugee.pk) + imagePath[-4:]
	return render(
		request,
		'RefugeeCard.html',
		{'refugee': refugee, 'imagePath': imagePath}
	)


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
			filePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
			filePath = filePath + '/media/' + str(refugee.pk) + refImage.name[-4:]
			fs.save(filePath, refImage)

			recognized_faces = kairos_face.recognize_face(
				file=filePath, gallery_name=gallery_name
			)
			print(recognized_faces)

			try:
				confidence = recognized_faces["images"][0]["candidates"][0]["confidence"]
				if(confidence > 0.7):
					print("You are fraud")
					form = RefugeeForm()
					return render(request, 'RefugeeForm.html', {'form': form})
			except KeyError:
				pass

			kairos_face.enroll_face(
				file=filePath, subject_id=str(refugee.pk), gallery_name=gallery_name
			)

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
