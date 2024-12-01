from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def clock(request):
    return render(request, 'clock/clock.html')
