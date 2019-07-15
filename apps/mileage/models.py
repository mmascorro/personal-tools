from django.db import models

class Trip(models.Model):
    name = models.TextField(max_length=60)

class Leg(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    start_miles = models.IntegerField()
    end_date = models.DateTimeField(null=True, blank=True)
    end_miles = models.IntegerField(null=True, blank=True)

    def get_total(self):
        if self.end_miles:
            return self.end_miles - self.start_miles
        else:
            return None