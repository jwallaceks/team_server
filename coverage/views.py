from django.views import generic
from django.contrib import messages
import grequests

from .models import Color


def cover(request, staff, command):
    staff_members = Color.objects.all()
    urls = []
    if command == "release":
        for st in staff_members:
            url = "http://{}.oeie.org:5138/blink1/on".format(st.staff)
            urls +=[url,]
#            r = requests.get(url)
            #if r.status_code == 200:
            #    messages.success(request, "{}'s light was notified.".format(st.staff))
            #else:
            #    messages.error(request, "{}'s light was NOT notified.".format(st.staff))
    elif command == "cover":
        color = Color.objects.get(staff=staff)
        for st in staff_members:
            url = "http://{}.oeie.org:5138/blink1/fadeToRGB?rgb=%23".format(st.staff, color.color)
            urls += [url, ]
            #r = requests.get(url, timeout=0.001)
            #if r.status_code == 200:
            #    messages.success(request, "{}'s light was notified.".format(st.staff))
            #else:
            #    messages.error(request, "{}'s light was NOT notified.".format(st.staff))
    rs = (grequests.get(u) for u in urls)
    grequests.map(rs)