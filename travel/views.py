from django.shortcuts import render,redirect
from .models import TouristArea,Hotel
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request,'home.html')

def touristAreas(request):
    areas = TouristArea.objects.all()
    param = {"areas":areas}
    return render(request,'touristAreas.html',param)

def newArea(request):
    area_name = request.POST.get('name')
    area_district = request.POST.get('district')
    area_upazilla = request.POST.get('upazilla')
    area_distanceFromDhaka = request.POST.get('distanceFromDhaka')
    area = TouristArea(name = area_name,district = area_district, upazilla = area_upazilla,distanceFromDhaka=area_distanceFromDhaka)
    if request.FILES['image']:
        image = request.FILES.get('image')
        area.image =image
        area.image.name=area.name+".jpg"
    area.save()
    return redirect("TouristAreas")


def addNewArea(request):
    return render(request,'newAreaForm.html')

def hotels(request):
    hotels = Hotel.objects.all()
    param = {"hotels":hotels}
    return render(request,'hotels.html',param)