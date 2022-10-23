from django.urls import path
from . import views
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static  
  
urlpatterns = [
    path("",views.home,name="Home"),
    path("area",views.touristAreas,name="TouristAreas"),
    path("addNewArea",views.addNewArea,name="addNewArea"),
    path("newArea",views.newArea,name="newArea"),
    path("hotel",views.hotels,name="Hotels"),
    
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  