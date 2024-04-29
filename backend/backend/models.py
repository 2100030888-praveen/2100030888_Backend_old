
from django.db import models

class Countries(models.Model):
    country_id = models.CharField(max_length=2, primary_key=True)
    country_name = models.CharField(max_length=50)
    region_id = models.IntegerField()

    def __str__(self):
        return self.country_name

class Locations(models.Model):
    location_id = models.IntegerField(primary_key=True)
    street_address = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=12)
    city = models.CharField(max_length=30)
    state_province = models.CharField(max_length=25, null=True, blank=True)  # Assuming it can be null
    country_id = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.street_address}, {self.city}'
