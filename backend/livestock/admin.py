from django.contrib import admin
from .models import Breed, Paddock, Animal, WeightRecord
# Register your models here.

admin.site.register(Breed)
admin.site.register(Paddock)
admin.site.register(Animal)
admin.site.register(WeightRecord)