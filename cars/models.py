from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=30, blank=True)
    # mileage = models.PositiveIntegerField(default=0)
    vin = models.CharField("VIN", max_length=17, unique=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model} {self.color}"

class Maintenance(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='maintenance_records')
    date = models.DateField()
    service_type = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.service_type}"
