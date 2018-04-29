from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


class Diary(models.Model):
    author = models.CharField(max_length=50, default=None)
    villageName = models.CharField(_('Village Name'), max_length=500, default=None)
    villageCode = models.CharField(_('Village Code'), max_length=50, default=None)

    # Shreni choices
    SHRENI_FOUR = '4'
    SHRENI_FIVE = '5'
    SHRENI_SIX = '6'

    SHRENI_CHOICES = (

        (SHRENI_FOUR, 'Shreni Four'),
        (SHRENI_FIVE, 'Shreni Five'),
        (SHRENI_SIX, 'Shreni Six'),
    )

    shreni = models.CharField(
        choices=SHRENI_CHOICES,
        max_length=100
    )

    distanceRoad = models.FloatField(_('Distance from road'), default=None)

    gataNumber = models.IntegerField(_('Gata Number'), default=None)
    area = models.IntegerField(default=None)
    connectivity = models.BooleanField()
    allotted = models.BooleanField(default=False)
    latitudeCoordinate = models.CharField(_('Latitude Coordinate'), max_length=15, default=None)
    longitudeCoordinate = models.CharField(_('Longitude Coordinate'), max_length=15, default=None)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)
    image1 = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    image2 = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    # unique id - villageCode + shreni + gataNumber
    uniqueId = models.CharField(_('Unique ID'), max_length=100, default=None)

    def __str__(self):
        return str(self.uniqueId)


class dataEntryEmployee(models.Model):
    employeeCode = models.CharField(_('Employee Code'), max_length=50)
    numberDataInput = models.IntegerField(_('Number Data Input'),)
    dataUniqueIdList = models.CharField(_('Data Unique ID List'), max_length=1000000)

    def __str__(self):
        return str(self.employeeCode)
