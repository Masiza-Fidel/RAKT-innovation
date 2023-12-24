from django.db import models

class FoodTruck(models.Model):
    location_id = models.IntegerField()
    applicant = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=255)
    cnn = models.IntegerField()
    location_description = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    block_lot = models.CharField(max_length=255)
    block = models.CharField(max_length=255)
    lot = models.CharField(max_length=255)
    permit = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    food_items = models.TextField()
    x = models.FloatField()
    y = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    schedule = models.CharField(max_length=255)
    dayshours = models.CharField(max_length=255)
    noi_sent = models.CharField(max_length=255)
    received = models.DateField()
    prior_permit = models.IntegerField()
    location = models.CharField(max_length=255)
    fire_prevention_districts = models.IntegerField()
    police_districts = models.IntegerField()
    supervisor_districts = models.IntegerField()
    zip_codes = models.IntegerField()
    neighborhoods_old = models.IntegerField()

    def __str__(self):
        return f"{self.location_id} - {self.applicant}"
