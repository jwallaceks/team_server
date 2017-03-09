from django.views import generic
from django.contrib import messages
from .models import Color
import subprocess
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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

    return HttpResponse("Coverage updated.")

@csrf_exempt
def release(request):
    rc = subprocess.call("/srv/sites/team_server/coverage/release.sh")
    return HttpResponse("Coverage updated.")


def index(request):
    return HttpResponse("Run a different command to update coverage.")