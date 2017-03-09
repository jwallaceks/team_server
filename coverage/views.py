from django.views import generic
from django.contrib import messages
from .models import Color
import subprocess

def cover(request, staff):
    if staff=="joel":
        rc = subprocess.call("/srv/sites/team_server/coverage/joel.sh")
    if staff=="trent":
        rc = subprocess.call("/srv/sites/team_server/coverage/trent.sh")
    if staff=="jessie":
        rc = subprocess.call("/srv/sites/team_server/coverage/jessie.sh")
    if staff=="zac":
        rc = subprocess.call("/srv/sites/team_server/coverage/zac.sh")

def release(request):
    rc = subprocess.call("/srv/sites/team_server/coverage/release.sh")