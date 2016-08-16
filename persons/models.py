from django.db import models
from places.models import Place



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
        blank=True, unique=True, max_length=100,
        help_text="ID, übernommen aus 'Kramer, Gefallene Tirols'")
    name = models.CharField(max_length=200, blank=True, help_text="Nachname des Verstorbenen")
    vorname = models.CharField(max_length=200, blank=True, help_text="Vorname des Verstorbenen")
    alter = models.CharField(
        blank=True, null=True, max_length=30, help_text="Alter zum Zeitpunkt des Todes")
    beruf = models.ForeignKey(Beruf, null=True, blank=True, help_text="Beruf des Verstorbenen")
    beruf_original = models.CharField(
        max_length=500, blank=True, help_text="Beruf wie in der Quelle angeführt")
    geburtsort = models.ForeignKey(
        Place, null=True, blank=True, verbose_name="Geburts- und/oder Wohnort",
        related_name="geburtsort")
    sterbeort = models.ForeignKey(
        Place, null=True, blank=True, verbose_name="Ort des Todes und/oder Ort der Beerdigung",
        related_name="sterbeort")
    todesart = models.ForeignKey(Todesart, null=True, blank=True)
    todesart_original = models.CharField(
        max_length=500, blank=True, help_text="Todesart wie in der Quelle angeführt")
    todesjahr = models.IntegerField(null=True, blank=True)
    todesmonat = models.IntegerField(null=True, blank=True)
    todestag = models.IntegerField(null=True, blank=True)
    todestag_original = models.CharField(
        max_length=500, blank=True, help_text="Sterbedatum wie in der Quelle angeführt")
    anmerkung = models.TextField(blank=True, help_text="Platz für Anmerkungen.")
    quelle = models.TextField(
        null=True, blank=True, help_text="Angabe einer alternativen Quelle.")

    def __str__(self):
        return "{}, {}".format(self.name, self.vorname)
