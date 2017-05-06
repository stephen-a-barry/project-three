# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def main(request):
    races = Race.objects.all()

    return render(request, 'horse/main.html', context={
        'races': races,
    })
