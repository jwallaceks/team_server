from django.views import generic
from django.contrib import messages
import requests
from django.http import HttpResponseRedirect

from .models import Color


def callback_function(response):
    if response.code == 200:
        return 0
    else:
        return 1


def cover(request, staff, command):
    staff_members = Color.objects.exclude(staff="joel")
    if command == "release":
        for st in staff_members:
            url = "http://{}.oeie.org:5138/blink1/on".format(st.staff)
            print(url)
            r = request.get(url)
            #if r.status_code == 200:
            #    messages.success(request, "{}'s light was notified.".format(st.staff))
            #else:
            #    messages.error(request, "{}'s light was NOT notified.".format(st.staff))
        url = "http://joel.oeie.org:5138/blink1/on"
        print(url)
        r = request.get(url)
    elif command == "cover":
        color = Color.objects.get(staff=staff)
        for st in staff_members:
            url = "http://{}.oeie.org:5138/blink1/fadeToRGB?rgb=%23{}".format(st.staff, color.color)
            print(url)
            r = requests.get(url)
            #if r.status_code == 200:
            #    messages.success(request, "{}'s light was notified.".format(st.staff))
            #else:
            #    messages.error(request, "{}'s light was NOT notified.".format(st.staff))
        url = "http://joel.oeie.org:5138/blink1/fadeToRGB?rgb=%23{}".format(color.color)
        print(url)
        r = request.get(url)
    return HttpResponseRedirect('/')

