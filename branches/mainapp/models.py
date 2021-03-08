from django.db import models


class Branch(models.Model):
    branch_name = models.CharField('Branch name', max_length=100)
    facade_image = models.ImageField(null=True, blank=True)
    latitude = models.CharField('Latitude', max_length=100)
    longitude = models.CharField('Longitude', max_length=100)

    def __str__(self):
        return self.branch_name

    class Meta:
        ordering = ('branch_name',)


class Employee(models.Model):
    first_name = models.CharField('First name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    position_title = models.TextField('Position')
    branch_name = models.ForeignKey(
        Branch,
        related_name='employees',
        on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name

    class Meta:
        ordering = ('last_name',)