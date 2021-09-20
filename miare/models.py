from django.db import models


class Courier(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Shift(models.Model):
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return f'{self.start} - {self.end}'


class Area(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Capacity(models.Model):
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    date = models.DateField()
    capacity = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Capacities'
        unique_together = [('shift', 'area', 'date'), ]


class CourierShift(models.Model):

    courier = models.ForeignKey(
        to=Courier,
        on_delete=models.CASCADE
    )

    area = models.ForeignKey(
        to=Area,
        on_delete=models.CASCADE
    )

    shift = models.ForeignKey(
        to=Shift,
        on_delete=models.CASCADE
    )

    shift_begin = models.DateField()

    shift_end = models.DateField()

