# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Race

# Register your models here.
class RaceAdmin(admin.ModelAdmin):
    list_display = ['race_name']

admin.site.register(Race, RaceAdmin)
