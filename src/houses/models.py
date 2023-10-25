from django.core.validators import RegexValidator
from django.db import models


class City(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class Address(models.Model):
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    street = models.CharField()
    zip_code = models.CharField(validators=[
        RegexValidator(r"^[0-9]+[0-9]+\-[0-9]+[0-9]+[0-9]+$",
                       "IP address should be numeric.")
    ])
    house_number = models.CharField()
    flat_number = models.IntegerField(blank=True,
                                      null=True)

    def is_flat_number(self):
        return f"/{self.flat_number}" if self.flat_number else ""

    def __str__(self):
        return f"{self.city}, {self.street} {self.house_number}{self.is_flat_number()}"


class House(models.Model):
    name = models.CharField(unique=True)

    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
