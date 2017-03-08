from django.views import generic
from django.contrib import messages
import requests

from .models import Color


def cover(request, staff, command):
    staff_members = Color.objects.all()
    if command == "release":
        for st in staff_members:
            url = "{}.oeie.org:5138/blink1/on".format(st.staff)
            r = requests.get(url)
            if r.status_code == 200:
                messages.success(request, "{}'s light was notified.".format(st.staff))
            else:
                messages.error(request, "{}'s light was NOT notified.".format(st.staff))
    elif command == "cover":
        color = Color.objects.get(staff=staff)
        for st in staff_members:
            url = "{}.oeie.org:5138/blink1/fadeToRGB?rgb=%23".format(st.staff, color.color)
            r = requests.get(url)
            if r.status_code == 200:
                messages.success(request, "{}'s light was notified.".format(st.staff))
            else:
                messages.error(request, "{}'s light was NOT notified.".format(st.staff))