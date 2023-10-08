from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class Producers(models.Model):
    name = models.CharField()
    active = models.BooleanField(default=False)
    website = models.URLField(blank=True,
                              null=True)
    comment = models.TextField(blank=True,
                               null=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


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

    rooms = models.ManyToManyField(Room)

    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name



class Devices(models.Model):
    THERMAL = 'the'
    HUMIDITY = 'hum'
    THERMAL_AND_HUMIDITY = 'tah'

    TYPES_CHOICES = (
        (THERMAL, 'Thermal'),
        (HUMIDITY, 'Humidity'),
        (THERMAL_AND_HUMIDITY, 'Thermal and Humidity'),
    )

    HTTP = 'http'

    PROTOCOL_CHOICES = (
        (HTTP, 'http'),
    )

    name = models.CharField()
    producer = models.ForeignKey(Producers,
                                 on_delete=models.CASCADE)
    api_url = models.URLField(null=True,
                              blank=True)
    type = models.CharField(choices=TYPES_CHOICES)
    house = models.ForeignKey(House,
                              on_delete=models.DO_NOTHING)

    active = models.BooleanField(default=True)

    ip_address = models.CharField(validators=[
        RegexValidator(r"^[0-9]+[0-9]?[0-9]?\.[0-9]+[0-9]?[0-9]?\.[0-9]+[0-9]?[0-9]?\.[0-9]+[0-9]?[0-9]?$",
                       "IP address should be numeric like '0.0.0.0'.")
    ])

    port = models.IntegerField()
    protocol = models.CharField(choices=PROTOCOL_CHOICES, default=HTTP)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('type',)
