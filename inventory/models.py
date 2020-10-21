from django.db import models

# Create your models here.

class Device(models.Model):
    type = models.CharField(max_length=100, blank=False)
    price = models.IntegerField()

    choices = (
        ('AVAILABLE','Item ready'),
        ('SOLD','Item Sold'),
        ('RESTOCKING','Item Restocking in few days'),

    )

    status = models.CharField(max_length=10, choices=choices, default="SOLD")
    issues = models.CharField(max_length=100, default="No Issues")

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type : {0} Price : {1}'.format(self.type, self.price)

class Laptop(Device):
    pass

class Desktop(Device):
    pass

class Mobile(Device):
    pass