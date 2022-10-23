from django.db import models


class TouristArea(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    upazilla = models.CharField(max_length=50)
    distanceFromDhaka =models.IntegerField(default=0)
    image = models.ImageField(upload_to='area_img',null=True,blank=True)

    def __str__(self):
        return self.name

    def totalHotel(self):
        a=Hotel.objects.filter(touristArea=self).count()
        return a




class Hotel(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    touristArea = models.ForeignKey(
        TouristArea,
        on_delete = models.CASCADE
    )
    def __str__(self):
        return self.name


class BusService(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    fairFromDhaka = models.IntegerField(default=0)
    touristArea = models.ForeignKey(
        TouristArea,
        on_delete = models.CASCADE
    )
    def __str__(self):
        return self.name
