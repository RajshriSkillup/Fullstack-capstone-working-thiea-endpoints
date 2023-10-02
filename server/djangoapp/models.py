from django.db import models
from django.utils.timezone import now

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return "Name: " + self.name + ", " + "Description: " + self.description

class CarModel(models.Model):
    carmake = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=100)
    dealer_id = models.IntegerField()

    # Choices for the car_type field as tuples
    TYPE_CHOICES = [
        ('Sedan', "Sedan"),
        ('SUV', "SUV"),
        ('Wagon', "Wagon")
    ]

    car_type = models.CharField(
        null=False,
        max_length=20,
        choices=TYPE_CHOICES,
        default='Sedan'
    )

    year = models.DateField()

    def __str__(self):
        return "Name: " + self.name + ", " \
               "Carmake: " + str(self.carmake) + ", " \
               "Type: " + self.car_type + ", " \
               "Year: " + str(self.year)


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
