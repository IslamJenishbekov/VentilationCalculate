from django.db import models
from projects.models import Project

class FinishedProducts(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    connection = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    area = models.FloatField()
    price_per = models.FloatField()
    unit_of_measurement = models.CharField(
        max_length=10,
        choices=[
            ('шт', 'Штуки'),
            ('м2', 'Квадратные метры')
        ]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Finished Product'
        verbose_name_plural = 'Finished Products'


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    price_per = models.FloatField()
    unit_of_measurement = models.CharField(
        max_length=10,
        choices=[
            ('шт', 'Штуки'),
            ('м2', 'Квадратные метры')
        ]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipment'


class Services(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    area = models.FloatField()
    price_per = models.FloatField()
    unit_of_measurement = models.CharField(
        max_length=10,
        choices=[
            ('шт', 'Штуки'),
            ('м2', 'Квадратные метры')
        ]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class FinishedProductToProject(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    finished_product = models.ForeignKey('FinishedProducts', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.project} - {self.finished_product}"

    class Meta:
        verbose_name = 'Finished Product to Project'
        verbose_name_plural = 'Finished Products to Projects'


class ServiceToProject(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    service = models.ForeignKey('Services', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.project} - {self.service}"

    class Meta:
        verbose_name = 'Service to Project'
        verbose_name_plural = 'Services to Projects'


class EquipmentToProject(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.project} - {self.equipment}"

    class Meta:
        verbose_name = 'Equipment to Project'
        verbose_name_plural = 'Equipment to Projects'
