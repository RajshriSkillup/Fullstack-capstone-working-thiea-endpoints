from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.
@admin.register(CarMake)
class CarMake(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(CarModel)
class CarModel(admin.Model.Admin):
    list_display = ('name', 'carmake', 'type', 'year')

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
