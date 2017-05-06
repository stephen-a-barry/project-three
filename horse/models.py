# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Race(models.Model):
    race_name = models.CharField(max_length=100, default='Kentucky Derby', choices=(
        ('Kentucky Derby', 'Kentucky Derby'),
        ('Preakness', 'Preakness'),
        ('Belmont Stakes', 'Belmont Stakes'),
        ('Breeders Cup Classic', 'Breeders Cup Classic'),
    ))
    # TODO: Find out how to do this with models.IntegerField
    number_of_horses = models.CharField(max_length=2, default='20', choices=(
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
    ))
    name_horse_1 = models.CharField(max_length=200, default="None")
    name_horse_2 = models.CharField(max_length=200, default="None")
    name_horse_3 = models.CharField(max_length=200, default="None")
    name_horse_4 = models.CharField(max_length=200, default="None")
    name_horse_5 = models.CharField(max_length=200, default="None")
    name_horse_6 = models.CharField(max_length=200, default="None")
    name_horse_7 = models.CharField(max_length=200, default="None")
    name_horse_8 = models.CharField(max_length=200, default="None")
    name_horse_9 = models.CharField(max_length=200, default="None")
    name_horse_10 = models.CharField(max_length=200, default="None")
    name_horse_11 = models.CharField(max_length=200, default="None")
    name_horse_12 = models.CharField(max_length=200, default="None")
    name_horse_13 = models.CharField(max_length=200, default="None")
    name_horse_14 = models.CharField(max_length=200, default="None")
    name_horse_15 = models.CharField(max_length=200, default="None")
    name_horse_16 = models.CharField(max_length=200, default="None")
    name_horse_17 = models.CharField(max_length=200, default="None")
    name_horse_18 = models.CharField(max_length=200, default="None")
    name_horse_19 = models.CharField(max_length=200, default="None")
    name_horse_20 = models.CharField(max_length=200, default="None")

    # TODO: add year field

    class Meta:
        ordering = ['race_name']

    def __str__(self):
        return self.race_name
