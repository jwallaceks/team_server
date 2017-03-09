from django.views import generic
from django.contrib import messages
from .models import Color
import subprocess
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def cover(request):
    staff = request.POST['user_name']

    if staff=="joel":
        rc = subprocess.call("/srv/sites/team_server/coverage/joel.sh")
    if staff=="trent":
        rc = subprocess.call("/srv/sites/team_server/coverage/trent.sh")
    if staff=="jessie":
        rc = subprocess.call("/srv/sites/team_server/coverage/jessie.sh")
    if staff=="zac":
        rc = subprocess.call("/srv/sites/team_server/coverage/zac.sh")
    return JsonResponse({"response_type": "in_channel","text": "Coverage updated. {} is now covering the phone.".format(staff)})



@csrf_exempt
def release(request):
    staff = request.POST['user_name']
    rc = subprocess.call("/srv/sites/team_server/coverage/release.sh")
    return JsonResponse(
        {"response_type": "in_channel", "text": "{} released coverage. Someone please cover the phone.".format(staff)})


def index(request):
    return HttpResponse("Run a different command to update coverage.")