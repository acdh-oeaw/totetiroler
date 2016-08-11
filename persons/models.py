from django.db import models


class Beruf(models.Model):
    name = models.CharField(blank=True, max_length=200, help_text="Beruf des Verstorbenen")

    def __str__(self):
        return self.name


class Todesart(models.Model):
    name = models.CharField(max_length=200, blank=True, help_text="Art und Weise des Ablebens")

    def __str__(self):
        return self.name


class Person(models.Model):
    kramer_index = models.CharField(
        unique=True, help_text="ID, übernommen aus 'Kramer, Gefallene Tirols'", max_length=100)
    name = models.CharField(max_length=200, blank=True, help_text="Nachname des Verstorbenen")
    vorname = models.CharField(max_length=200, blank=True, help_text="Vorname des Verstorbenen")
    alter = models.CharField(
        blank=True, null=True, max_length=30, help_text="Alter zum Zeitpunkt des Todes")
    beruf = models.ForeignKey(Beruf, null=True, blank=True, help_text="Beruf des Verstorbenen")
