from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Color
import requests

@shared_task
def release(staff):
    url = "http://{}.oeie.org:5138/blink1/on".format(staff)
    print(url)
    r = requests.get(url)
    return r

@shared_task
def coverage(color, staff):
    url = "http://{}.oeie.org:5138/blink1/fadeToRGB?rgb=%23{}".format(staff, color.color)
    print(url)
    r = requests.get(url)
    return r