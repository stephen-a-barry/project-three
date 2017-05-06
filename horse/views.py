# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Race

# Create your views here.
def main(request):
    races = Race.objects.all()
    kentucky_derby = Race.objects.filter(race_name="Kentucky Derby")

    return render(request, 'horse/main.html', context={
        'races': races,
        'kentucky_derby': kentucky_derby,
    })
