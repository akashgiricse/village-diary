from django.db import models

# Create your models here.


class Diary(models.Model):
    author = models.CharField(max_length=50, default=None)
    villageName = models.CharField(max_length=500, default=None)
    villageCode = models.CharField(max_length=50, default=None)

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

    distanceRoad = models.FloatField(default=None)

    gataNumber = models.IntegerField(default=None)
    area = models.IntegerField(default=None)
    connectivity = models.BooleanField()
    allotted = models.BooleanField(default=False)
    latitudeCoordinate = models.CharField(max_length=15, default=None)
    longitudeCoordinate = models.CharField(max_length=15, default=None)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)
    image1 = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    image2 = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    # unique id - villageCode + shreni + gataNumber
    uniqueId = models.CharField(max_length=100, default=None)

    def __str__(self):
        return str(self.uniqueId)


class dataEntryEmployee(models.Model):
    employeeCode = models.CharField(max_length=50)
    numberDataInput = models.IntegerField()
    dataUniqueIdList = models.CharField(max_length=1000000)

    def __str__(self):
        return str(self.employeeCode)