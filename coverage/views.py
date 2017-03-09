from django.views import generic
from django.contrib import messages
import requests
from django.http import HttpResponseRedirect
import celery
from .models import Color
from .tasks import release,coverage

def cover(request, staff, command):
    staff_members = Color.objects.exclude(staff="joel")
    if command == "release":
        for st in staff_members:
            release.delay(st.staff)
    elif command == "cover":
        color = Color.objects.get(staff=staff)
        for st in staff_members:
            coverage(color, st.staff)
    return HttpResponseRedirect('/')

