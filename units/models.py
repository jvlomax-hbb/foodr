from django.db import models


# Create your models here.
class UnitCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=255, unique=True)
    symbol = models.CharField(max_length=20, unique=True)
    category = models.ForeignKey(UnitCategory, on_delete=models.CASCADE, related_name="units")

    def __str__(self):
        return self.name


class UnitConversionRatio(models.Model):
    from_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="from_unit")
    to_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="to_unit")
    ratio = models.FloatField()

    def __str__(self):
        return f"{self.from_unit.symbol} -> {self.to_unit.symbol}"
