from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User
from core.services.strava2kml import strava2kml
import json
import requests

def authenticate(request):
  json_body = json.loads(request.body.decode('utf-8'))
  code = json_body.get('code')
  r = requests.post('https://www.strava.com/oauth/token', data={
    'client_id': 28106,
    'client_secret': settings.STRAVA_CLIENT_SECRET,
    'code': code,
    'grant_type': 'authorization_code'
  })
  strava_content = r.json()
  print(strava_content)
  username = strava_content['athlete']['username']
  user = User.objects.filter(username=username).first()
  if not user:
    first_name = strava_content['athlete']['firstname']
    last_name = strava_content['athlete']['lastname']
    username = strava_content['athlete']['username']
    user = User(email='{username}@gmail.com'.format(username=username), first_name=first_name, last_name=last_name, username=username)
    user.save()
  user.profile.strava_auth_token = strava_content['access_token']
  user.profile.strava_refresh_token = strava_content['refresh_token']
  user.profile.save()
  login(request, user)
  return HttpResponse(status=204)

def get_strava_kml(request, username, seed):
  response = HttpResponse(strava2kml(username), content_type='application/vnd.google-earth.kml+xml')
  response['Content-Disposition'] = 'attachment; filename=strava.kml'
  response['Access-Control-Allow-Origin'] = '*'
  response['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
  return response