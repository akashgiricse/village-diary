from django.db import models

# Create your models here.


class Diary(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    villageName = models.CharField(max_length=500)
    villageCode = models.IntegerField(max_length=100)
    # Shreni choices
    SHRENI_FOUR = 'Four'
    SHRENI_FIVE = 'Five'
    SHRENI_SIX = 'Six'

    SHRENI_CHOICES = (

        (SHRENI_FOUR, 'Shreni Four'),
        (SHRENI_FIVE, 'Shreni Five'),
        (SHRENI_SIX, 'Shreni Six'),
    )

    shreni = models.CharField(
        choices=SHRENI_CHOICES
    )
    # Distance from road choices
    DISTANCE_MORE_THAN_ONE = 'more_than_one'
    DISTANCE_LESS_THAN_ONE = 'less_than_one'

    DISTANCE_CHOICES = (

        (DISTANCE_MORE_THAN_ONE, 'More than one'),
        (DISTANCE_LESS_THAN_ONE, 'Less than one'),
    )

    distanceRoad = models.CharField(
        choices=DISTANCE_CHOICES
    )

    gataNumber = models.IntegerField(max_length=100)
    area = models.IntegerField(max_length=100)
    connectivity = models.BooleanField()
    allotted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)
